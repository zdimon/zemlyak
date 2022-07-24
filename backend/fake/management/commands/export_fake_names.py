from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import Cafe, City
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
        print('Load fake names')
        source = os.path.join(FIXTURES_PATH, 'fake/names.json')
        if os.path.exists(source):
            os.remove(source)
        else:
            print("Can not delete city-ua.json as it doesn't exists")
        out = {
            "man": [],
            "woman": []
        }
        filem = os.path.join(FIXTURES_PATH, 'fake/mnames.txt')
        
        with open(filem,'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line)>2:
                    print(f'-{line}-')
                    name_ru = line
                    name_uk = translator.translate(line,src='ru', dest='uk').text
                    name_en = translator.translate(line,src='ru', dest='en').text
                    print(name_en)
                    rec = {
                        "name_ru": name_ru,
                        "name_uk": name_uk,
                        "name_en": name_en,
                        "gender": "m"
                    }
                    out["man"].append(rec)


        filew = os.path.join(FIXTURES_PATH, 'fake/wnames.txt')
        
        with open(filew,'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line)>2:
                    print(f'-{line}-')
                    name_ru = line
                    name_uk = translator.translate(line,src='ru', dest='uk').text
                    name_en = translator.translate(line,src='ru', dest='en').text
                    print(name_en)
                    rec = {
                        "name_ru": name_ru,
                        "name_uk": name_uk,
                        "name_en": name_en,
                        "gender": "w"
                    }
                    out["woman"].append(rec)


        with open(source, 'w') as f:
            f.write(json.dumps(out))
        print('Done!')
        