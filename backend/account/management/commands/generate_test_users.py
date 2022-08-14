import json
from django.core.management.base import BaseCommand, CommandError
from account.models import City, Country, Cafe
import json
from .utils import user_gen




class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Generate city json files')
        country = Country.objects.get(alias='ukraine')
        cities = City.objects.filter(country=country)
        for city in cities:
            print(city.alias)
            for cityin in cities:
                user_gen(city.alias,cityin.alias)
