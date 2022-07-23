from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import City, Country
import requests
from backend.settings import API_URL
import os
import requests
from bs4 import BeautifulSoup
import csv
import json
import re
from googletrans import Translator
import os


def clear_str(str):
    o = str.replace('\xa0','')
    o = o.replace('\n','')
    return o

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

translator = Translator()

class Command(BaseCommand):

    def handle(self, *args, **options):
        source = f'{FIXTURES_PATH}/city/city-ua.json'
        if os.path.exists(source):
            os.remove(source)
        else:
            print("Can not delete city-ua.json as it doesn't exists")
        print('Loading city from')
        t = translator.translate('Киев', src='ru')
        print(t.text)
        out = []

        pt = f'{FIXTURES_PATH}/city/city-ua.csv'
        with open(pt, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in spamreader:
                #print(row[2])
                out1 = re.sub('\(.*?\)', '', row[0])
                out2 = re.sub('\[.*?\]', '', out1)
                name_ru = clear_str(out2)
                name_uk = clear_str(find_between(row[0],'(укр.',')'))
                name_en = translator.translate(name_ru, src='ru').text

                region_ru = clear_str(row[2])
                region_en = translator.translate(clear_str(row[2]),src='ru', dest='en').text
                region_uk = translator.translate(clear_str(row[2]),src='ru', dest='uk').text


                rec = {}
                rec["name_ru"] = name_ru
                rec["name_uk"] = name_uk
                rec["name_en"] = name_en
                rec["region_ru"] = region_ru
                rec["region_uk"] = region_uk
                rec["region_en"] = region_en
                out.append(rec)
                #break
            print(out)
            with open(source, 'w') as f:
                f.write(json.dumps(out))


