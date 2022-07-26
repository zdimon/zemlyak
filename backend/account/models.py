from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from slugify import slugify
from backend.celery import app
from rest_framework.authtoken.models import Token

# channels
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Country(models.Model):
    name = models.CharField(default='', max_length=250)
    alias = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(default='', max_length=250)
    prof = models.CharField(default='', max_length=250)
    region = models.CharField(default='', max_length=250)
    alias = models.CharField(default='', max_length=250, null=True, blank=True)
    country_alias = models.CharField(max_length=250, default='', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    is_occupated = models.BooleanField(default=False)
    search = models.CharField(default='', max_length=250)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.alias = slugify(self.name_en)
        self.search = f'{self.name_ru.lower()} {self.name_en.lower()} {self.name_uk.lower()}'
        super(City, self).save(*args, **kwargs)



class CityGroup(models.Model):
    target = models.ForeignKey(City, on_delete=models.CASCADE, related_name="target")
    source = models.ForeignKey(City, on_delete=models.CASCADE, related_name="source")

    def __str__(self) -> str:
        return '%s -> %s' % (self.source, self.target)



class Cafe(models.Model):
    name = models.CharField(default='', max_length=250)
    link = models.CharField(default='', max_length=250)
    desc = models.TextField(default='')
    image = models.ImageField(upload_to='cafe')
    alias = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(default='')
    
        
    def __str__(self) -> str:
        return self.name

    def set_groups(self):
        from account.models import CityGroup
        for group in CityGroup.objects.filter(target=self.city):
            c2g = Cafe2Group()
            c2g.group = group
            c2g.cafe = self
            c2g.save()

class Cafe2Group(models.Model):
    group = models.ForeignKey(CityGroup, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

class UserProfile(User):
    GENDER = (
        ('male', _('Man')),
        ('female', _('Woman'))
    )

    gender = models.CharField(
        verbose_name=_('Gender'),
        choices=GENDER,
        db_index=True,
        default='male',
        max_length=6)

    publicname = models.CharField(default='', max_length=250)
    prof = models.CharField(default='', max_length=250)
    surename = models.CharField(default='', max_length=250)
    telegram = models.CharField(default='', max_length=250)
    is_online = models.BooleanField(default=False)
    is_fake = models.BooleanField(default=False)
    account = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    birthday = models.DateField(null=True, blank=True)
    source_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="source_country")
    source_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="source_city")
    target_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="target_country")
    target_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="target_city")
    group = models.ForeignKey(CityGroup, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return self.publicname

    def get_opposite_gender(self):
        if self.gender == 'male':
            return 'female'
        return 'male'

    def get_contacts(self):
        from contact.models import Contact
        return Contact.objects.filter(owner=self)

    def update_online(self):
        from online.models import SocketConnection
        cnt = SocketConnection.objects.filter(user = self).count()
        if cnt == 0:
            self.is_online = False
            self.save()
            self.user_offline_task.delay(self.id)
        else:
            self.is_online = True
            self.save()
            self.user_online_task.delay(self.id)
    
    """ def get_favourites(self):
        from favourite.models import Favourite
        return Favourite.objects.filter(owner=self) """

    @app.task
    def user_online_task(user_id):
        from account.serializers.profile import UserProfileSerializer
        payload_user = UserProfile.objects.get(pk=user_id)
        # print('User online task for %s token %s' % (user,token.key))
        channel_layer = get_channel_layer()
        for user in UserProfile.objects.filter(is_online=True, gender=payload_user.get_opposite_gender()):
            token = Token.objects.get(user=user)
            async_to_sync(channel_layer.group_send)( \
                token.key, \
                { \
                    'type': 'user_online', \
                    'message': UserProfileSerializer(payload_user).data \
                }) \

    @app.task
    def user_offline_task(user_id):
        from account.serializers.profile import UserProfileSerializer
        payload_user = UserProfile.objects.get(pk=user_id)
        # print('User online task for %s token %s' % (user,token.key))
        channel_layer = get_channel_layer()
        for user in UserProfile.objects.filter(is_online=True, gender=payload_user.get_opposite_gender()):
            token = Token.objects.get(user=user)
            async_to_sync(channel_layer.group_send)( \
                token.key, \
                { \
                    'type': 'user_offline', \
                    'message': UserProfileSerializer(payload_user).data \
                })


    @property
    def get_main_photo_url(self):
        from usermedia.models import UserMedia
        try:
            media = UserMedia.objects.get(user=self, is_main=True, type_media='photo')
            return media.get_small_image_url

        except Exception as i:
            return '/static/img/undraw_profile.svg' 

    @property
    def get_main_photo(self):
        return mark_safe('<img src="%s" />' % self.get_main_photo_url)  


class Meeting(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    message = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)