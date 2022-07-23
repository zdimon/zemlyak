from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import City, Country
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading country')
        Country.objects.all().delete()
        c = Country()
        c.name_ru = 'Украина'
        c.name_uk = 'Україна'
        c.name_ru = 'Ukraine'
        c.alias = 'ukraine'
        c.save()