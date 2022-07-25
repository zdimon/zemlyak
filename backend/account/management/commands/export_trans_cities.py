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
        print('Export trans city.....')
        for country in Country.objects.filter(~Q(alias='ukraine')):
            source = os.path.join(FIXTURES_PATH, f'city/{country.alias}.json')
            print(source)
            if exists(source):
                continue
            rec = {}
            rec["name_ru"] = country.name_ru
            rec["name_uk"] = country.name_uk
            rec["name_en"] = country.name_en
            rec["alias"] = country.alias
            rec["city"] = []   
            csource = os.path.join(FIXTURES_PATH, f'city_api/{country.alias}.json')
            try:
                with open(csource,'r') as f:
                    jdata = json.loads(f.read())
            except:
                print(f'Can not find {csource}!!!!')
                continue
            for city in jdata:
                try:
                    name_en = city['city']
                    name_ru = translator.translate(city['city'],src='en', dest='ru').text
                    name_uk = translator.translate(city['city'],src='en', dest='uk').text
                    region_en = city['state']
                    region_ru = translator.translate(city['state'],src='en', dest='ru').text
                    region_uk = translator.translate(city['state'],src='en', dest='uk').text
                    alias = city['city'].lower()
                    country_alias = country.alias.lower()
                    crec = {}
                    crec["name_ru"] = name_ru
                    crec["name_uk"] = name_uk
                    crec["name_en"] = name_en
                    crec["region_ru"] = region_ru
                    crec["region_uk"] = region_uk
                    crec["region_en"] = region_en
                    crec["alias"] = alias
                    crec["country_alias"] = country_alias
                    rec["city"].append(crec)
                except:
                    continue

            with open(source, 'w') as f:
                f.write(json.dumps(rec))
        print('Done')
           