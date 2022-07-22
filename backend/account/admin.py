from django.contrib import admin
from account.models import UserProfile, City, Country, CityGroup, Cafe, Cafe2Group
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from modeltranslation.admin import TranslationTabularInline

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
class CityAdmin(TabbedTranslationAdmin):
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
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

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