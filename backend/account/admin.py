from django.contrib import admin
from account.models import UserProfile, City, Country, CityGroup, Cafe, Cafe2Group
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
   
    list_display = [
        'get_main_photo',
        'username', 
        'gender', 
        'is_online', 
        'target_city',
        'target_country',
        'source_city',
        'source_country']

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    pass

@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = [
        'name',
        'country',
        'country_alias',
        'is_occupated'
    ]

@admin.register(CityGroup)
class CityGroupAdmin(admin.ModelAdmin):
    list_display = [
        'source',
        'target'
    ]

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'city'
    ]

@admin.register(Cafe2Group)
class Cafe2GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group',
        'cafe'
    ]