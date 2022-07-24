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
from slugify import slugify

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading country')
        file = f'{FIXTURES_PATH}/country.json'
        country = Country.objects.all().delete()
        with open(file,'r') as f:
            jdata = json.loads(f.read())
            for country in jdata:
                print(country['name_ru'])
                ct = Country()
                ct.name_ru = country['name_ru']
                ct.name_en = country['name_en']
                ct.name_uk = country['name_uk']
                ct.alias = slugify(country['name_en'].lower())
                ct.save()
                
