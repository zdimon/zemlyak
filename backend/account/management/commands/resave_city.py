from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import Cafe, City


class Command(BaseCommand):

    def handle(self, *args, **options):
        for city in City.objects.all():
            city.save()
            print(city)