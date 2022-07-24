
from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import Cafe, City, Country
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView
from googletrans import Translator
headers = {
	"X-RapidAPI-Key": "4992332789mshfb7baebbf8e1951p154cc3jsn9a44c55acbda",
	"X-RapidAPI-Host": "andruxnet-world-cities-v1.p.rapidapi.com"
}
translator = Translator()
from django.db.models import Q


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Export cities')
        url = "https://andruxnet-world-cities-v1.p.rapidapi.com/"

        #for country in Country.objects.filter(~Q(alias='Ukraine')):
        country = Country.objects.get(alias='australia')
        print(country)

        querystring = {"query":country.alias,"searchby":"country"}
        source = os.path.join(FIXTURES_PATH, f'city/{country.alias.capitalize()}.json')
        #print(querystring)

        response = requests.request("GET", url, headers=headers, params=querystring)

        with open(source, 'w') as f:
            f.write(response.text)

        print('Done!')