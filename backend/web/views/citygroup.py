from django.shortcuts import render
import requests
import json
from account.models import City, Country, UserProfile, CityGroup
from backend.settings import FIXTURES_PATH
from django.utils import translation
import os

def city_group(request,city):
    return render(request, 'web/city_group.html')