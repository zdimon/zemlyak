from django.core.management.base import BaseCommand, CommandError
import json
from account.models import UserProfile
from online.models import SocketConnection
from backend.settings import FIXTURES_PATH
import os
from slugify import slugify


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clear file names')
        dir_path = f'{FIXTURES_PATH}/city_api'
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                print(path)
                name = path.split('.')[0]
                nname = slugify(name) 
                oldp = os.path.join(dir_path, path)
                newp = os.path.join(dir_path, f'{nname}.json')
                os.rename(oldp, newp)
