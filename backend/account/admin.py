from django.contrib import admin
from account.models import UserProfile, City, Country
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
   
    list_display = [
        'get_main_photo',
        'username', 
        'gender', 
        'is_online', 
        'birthday']

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    pass

@admin.register(City)
class CityAdmin(TranslationAdmin):
    pass