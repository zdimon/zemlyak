from curses.ascii import EM
from django.core.management.base import BaseCommand
from mailing.models import EmailTemplate
from django.utils.translation import gettext_lazy as _
from backend.settings import FIXTURES_PATH
import json
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start loading email templates')
        source = os.path.join(FIXTURES_PATH, f'email.json')
        EmailTemplate.objects.all().delete()
        with open(source,'r') as f:
            jdata = json.loads(f.read())      
        for t in jdata:  
            tpl = EmailTemplate()
            tpl.alias = t["alias"]
            tpl.title_ru = t["title_ru"]
            tpl.title_en = t["title_en"]
            tpl.title_uk = t["title_uk"]
            tpl.content_ru = t["content_ru"]
            tpl.content_en = t["content_en"]
            tpl.content_uk = t["content_uk"]
            tpl.save()

      