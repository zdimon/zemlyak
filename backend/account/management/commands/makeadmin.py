from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Make admin')
        UserProfile.objects.filter(username='admin').delete()
        p = UserProfile()
        p.username = 'admin'
        p.set_password('admin')
        p.is_superuser = True
        p.save()