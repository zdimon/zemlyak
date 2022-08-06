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
from .utils import user_gen

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('opt', nargs='+', type=str)

    def handle(self, *args, **options):
        print('Generate user')
        print(options['opt'][0])
        user_gen(options['opt'][0])
    