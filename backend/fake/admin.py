from django.contrib import admin
from .models import Name, Prof

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'gender'
    ]

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    list_display = [
        'name_ru',
        'name_uk',
        'name_en'
    ]