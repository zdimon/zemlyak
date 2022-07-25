from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from fake.models import Prof, Name
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
from account.views.registration import RegistrationView
from fake.utils import make_user
from account.models import City, UserProfile

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading fake users')
        UserProfile.objects.all().delete()
        for source in City.objects.all():
            print(f'Loading for {source}')
            target = City.objects.all().order_by('?').first()
            make_user(source,target)
       