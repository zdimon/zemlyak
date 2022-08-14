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

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading cafe')
        user_file = os.path.join(FIXTURES_PATH,'cafe', 'uzhorod.json')
        #print(user_file)
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
        

        # cafe = Cafe()
        # cafe.name = 'Alex'
        # cafe.link = 'Odessa'
        # cafe.desc_ru = 
        # cafe.desc_en =
        # cafe.desc_uk =
        
        # cafe.save()       
    #print(jdata[1]["name"])
        jdata = [{"name": "cafe1"}, {"name": "cafe2"}]
        for cafe in jdata:
            print(cafe["name"])
            print(cafe["link"])
            cafe = Cafe()
            cafe.name = cafe["name"]
            cafe.save()

       

        #     Cafe.objects.all().delete()
        #     for cafe in jdata:
        #         city = City.objects.get(alias=cafe['city'])
        #         c = Cafe()
        #         c.name = cafe['name']
        #         c.link = cafe['link']
        #         c.desc_ru = cafe['desc_ru']
        #         c.desc_en = cafe['desc_en']
        #         c.desc_uk = cafe['desc_uk']
        #         c.city = city
        #         c.save()
        #         c.set_groups()
        #         print(cafe['name'])
              