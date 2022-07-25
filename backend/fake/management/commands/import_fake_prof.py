from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from fake.models import Prof
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading fake prof')
        user_file = f'{FIXTURES_PATH}/fake/prof.json'
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            #print(jdata)
        Prof.objects.all().delete
        for name in jdata:
            n = Prof()
            n.name_ru = name['name_ru']
            n.name_en = name['name_en']
            n.name_uk = name['name_uk']
            n.save()
            print(name)

                
