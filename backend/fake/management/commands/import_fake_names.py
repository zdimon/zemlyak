from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from fake.models import Name
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading fake names')
        user_file = f'{FIXTURES_PATH}/fake/names.json'
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            #print(jdata)
        Name.objects.all().delete
        for name in jdata['man']:
            n = Name()
            n.gender = 'm'
            n.name_ru = name['name_ru']
            n.name_en = name['name_en']
            n.name_uk = name['name_uk']
            n.save()
            print(name)
        for name in jdata['woman']:
            n = Name()
            n.gender = 'w'
            n.name_ru = name['name_ru']
            n.name_en = name['name_en']
            n.name_uk = name['name_uk']
            n.save()
            print(name)
                
