# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from account.models import UserProfile, City

class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    birthday = serializers.CharField() # if use DataField we can not define the validator
    gender = serializers.ChoiceField(choices=['male','female'])
    source_city = serializers.CharField()
    target_city = serializers.CharField()

    def validate_username(self, value):
        """
        Check that the name is unique.
        """
        error = False
        try:
            UserProfile.objects.get(username=value)
            error = True
        except:
            pass

        if error:
            raise serializers.ValidationError("This username is already exists!!!")
        return value

    def validate_birthday(self, value):
        """
            convert 2020-06-16T21:00:00.000Z -> 2020-06-16
        """
        return value.split('T')[0]


    def save(self):
        target_city = City.objects.get(alias=self.validated_data['target_city'])
        source_city = City.objects.get(alias=self.validated_data['source_city'])
        profile = UserProfile()
        profile.username = self.validated_data['username']
        profile.set_password(self.validated_data['password'])
        profile.birthday = self.validated_data['birthday']
        profile.gender = self.validated_data['gender']
        profile.target_city = target_city
        profile.target_country = target_city.country
        profile.source_city = source_city
        profile.source_country = source_city.country
        profile.save()
        return profile

