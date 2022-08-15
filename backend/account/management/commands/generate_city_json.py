import json
from django.core.management.base import BaseCommand, CommandError
from account.models import City, Country
PATH = '/media/zdimon/d04b3bc3-5060-4287-83eb-acecaca9c587/zemlyak/fixtures/cafe/'
import json
from os.path import exists

tpl =  '''[
    {
        "name": "",
        "link": "",
        "address_ru": "",
        "address_uk": "",
        "address_en": "",
        "desc_ru": "",
        "desc_en":  "",
        "desc_uk":  ""
    },
    {
        "name": "",
        "link": "",
        "address_ru": "",
        "address_uk": "",
        "address_en": "",
        "desc_ru": "",
        "desc_en":  "",
        "desc_uk":  ""
    },
    {
        "name": "",
        "link": "",
        "address_ru": "",
        "address_uk": "",
        "address_en": "",
        "desc_ru": "",
        "desc_en":  "",
        "desc_uk":  ""
    }

]'''


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Generate city json files')
        country = Country.objects.get(alias='ukraine')
        cities = City.objects.filter(country=country)
        for city in cities:
            print(city.alias)
            file_name = PATH+city.alias+'.json'
            print(file_name)
            if not exists(file_name):
                file = open(file_name,'w')
                file.write(tpl)
