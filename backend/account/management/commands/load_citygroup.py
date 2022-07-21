from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import City, Country, CityGroup
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading city group')
        CityGroup.objects.all().delete()
        for source in City.objects.all():
            for target in City.objects.filter(is_occupated=False):
                if source != target:
                    cg = CityGroup()
                    cg.source = source
                    cg.target = target
                    cg.save()
                    print('%s - %s' % (source, target))