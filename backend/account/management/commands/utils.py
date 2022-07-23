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


translator = Translator()

class Command(BaseCommand):

    def handle(self, *args, **options):
        translator = Translator()
        t = translator.translate('Перевод', src='ru', dest='uk')
        print(t.text)