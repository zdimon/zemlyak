import json
from django.core.management.base import BaseCommand, CommandError
from account.models import City, Country, Cafe
import json





class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Generate city json files')
        country = Country.objects.get(alias='ukraine')
        cities = City.objects.filter(country=country)
        Cafe.objects.all().delete()
        for city in cities:
            print(city.alias)
            c = Cafe()
            c.name = f'Cafe {city}'
            c.link = 'https://www.google.com/'
            c.desc_ru = f'Описание кафе {city}'
            c.desc_en = f'Description кафе {city}'
            c.desc_uk = f'Опис кафе {city}'
            c.address_ru = f'Адрес кафе {city}'
            c.address_en = f'Address кафе {city}'
            c.address_uk = f'Адрес кафе {city}'
            c.city = city
            c.save()