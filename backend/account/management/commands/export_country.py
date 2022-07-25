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
from googletrans import Translator
translator = Translator()


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading countries')
        file = f'{FIXTURES_PATH}/country.csv'
        source = f'{FIXTURES_PATH}/country.json'
        if os.path.exists(source):
            os.remove(source)
        else:
            print("Can not delete city-ua.json as it doesn't exists")
        #Country.objects.all().delete()
        out = []
        with open(file,'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                name_ru = line
                name_uk = translator.translate(line,src='ru', dest='uk').text
                name_en = translator.translate(line,src='ru', dest='en').text
                rec = {
                    "name_ru": name_ru,
                    "name_uk": name_uk,
                    "name_en": name_en,
                }
                out.append(rec)
        with open(source, 'w') as f:
            f.write(json.dumps(out))
        print('Done!')