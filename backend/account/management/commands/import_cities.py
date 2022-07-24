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

translator = Translator()

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading city')
        City.objects.filter(~Q(country_alias='ukraine')).delete()
        for country in Country.objects.filter(~Q(alias='Ukraine')):
            print(country)
            source = os.path.join(FIXTURES_PATH, f'city/{country.alias.capitalize() }.json')
            with open(source,'r') as f:
                jdata = json.loads(f.read())
            for city in jdata:
                print(city['city'])
                ct = City()
                ct.name_en = city['city']
                ct.name_ru = translator.translate(city['city'],src='en', dest='ru').text
                ct.name_uk = translator.translate(city['city'],src='en', dest='uk').text
                ct.region_en = city['state']
                ct.region_ru = translator.translate(city['state'],src='en', dest='ru').text
                ct.region_uk = translator.translate(city['state'],src='en', dest='uk').text
                ct.alias = city['city'].lower()
                ct.country_alias = country.alias.lower()
                ct.is_occupated = False
                ct.country = country
                ct.save()            