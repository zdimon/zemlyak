from django.contrib import admin
from account.models import UserProfile, City, Country, CityGroup, Cafe, Cafe2Group, Meeting
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from modeltranslation.admin import TranslationTabularInline


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
   
    list_display = ['user', 'cafe']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
   
    list_display = [
        'get_main_photo',
        'username', 
        'gender', 
        'is_online', 
        'target_city',
        'publicname',
        'source_city',
        'prof',
        'is_fake']

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = [
        'name_ru',
        'name_uk',
        'name_en',
        'alias'
    ]

@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_filter = ['country']
    list_display = [
        'name_ru',
        'name_uk',
        'name_en',
        'country',
        'region',
        'is_occupated',
        'alias',
        'search'
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