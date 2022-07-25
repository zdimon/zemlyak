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
from django.db.models import Q
from googletrans import Translator
from os.path import exists
translator = Translator()

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading city')
        City.objects.all().delete()
        for country in Country.objects.all():
            print(country)
            source = os.path.join(FIXTURES_PATH, f'city/{country.alias}.json')
            if not exists(source):
                continue            
            with open(source,'r') as f:
                jdata = json.loads(f.read())
            for city in jdata["city"]:
                print(city['name_ru'])
                ct = City()
                ct.name_en = city['name_en']
                ct.name_ru = city['name_ru']
                ct.name_uk = city['name_uk']
                ct.region_en = city['region_en']
                ct.region_ru = city['region_ru']
                ct.region_uk = city['region_uk']
                ct.alias = city['alias']
                ct.country_alias = city['country_alias']
                ct.is_occupated = False
                ct.country = country
                ct.save()            