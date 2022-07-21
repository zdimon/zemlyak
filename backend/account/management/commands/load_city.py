from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import City, Country
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading city')
        user_file = os.path.join(FIXTURES_PATH, 'city.json')
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            City.objects.all().delete()
            Country.objects.all().delete()
            for country in jdata:
                c = Country()
                c.name_ru = country['name_ru']
                c.name_en = country['name_en']
                c.name_uk = country['name_uk']
                c.alias = country['alias']
                c.save()
                print(country['name_ru'])
                for city in country['city']:
                    ct = City()
                    ct.name_ru = city['name_ru']
                    ct.name_en = city['name_en']
                    ct.name_uk = city['name_uk']
                    ct.alias = city['alias']
                    ct.country_alias = c.alias
                    ct.is_occupated = city['is_occupated']
                    ct.country = c
                    ct.save()
                    print(city['name_ru'])
                
