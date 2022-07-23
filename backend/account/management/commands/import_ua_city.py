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
        user_file = f'{FIXTURES_PATH}/city/city-ua.json'
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            #print(jdata)
            country = Country.objects.get(alias='ukraine')
            City.objects.filter(country=country).delete()
            for city in jdata:
                ct = City()
                ct.name_ru = city['name_ru']
                ct.name_en = city['name_en']
                ct.name_uk = city['name_uk']
                ct.region_ru = city['region_ru']
                ct.region_en = city['region_en']
                ct.region_uk = city['region_uk']
                ct.alias = city['name_en']
                ct.country_alias = country.alias
                ct.is_occupated = False
                ct.country = country
                ct.save()
                print(city['name_ru'])
                
