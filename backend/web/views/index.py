from django.shortcuts import render
import requests
import json
from account.models import City, Country, UserProfile, CityGroup
from backend.settings import FIXTURES_PATH
from django.utils import translation
import os

def homepage(request,country='ukraine',city=None):
    #res = requests.get('http://localhost:8000/v1/account/user_list')
    #data = json.loads(res.text)
    about_file = os.path.join(FIXTURES_PATH, f'about_{translation.get_language()}.md')
    with open(about_file,'r') as f:
        about = f.read()
    current_city = None
    if city:
        current_city = City.objects.get(alias=city)
    countries = Country.objects.all()
    current_country = Country.objects.get(alias=country)
    cities = City.objects.filter(country=current_country).order_by('name_ru')
    citygroups = []
    if current_city and current_country:
        users = UserProfile.objects.filter(target_city=current_city)
        citygroups = CityGroup.objects.filter(target=current_city)
    else:
        users = UserProfile.objects.filter(target_country=current_country)

    return render(request, 'main/index.html',{"countries": countries, "current_country": current_country, "cities": cities, "current_city": current_city, "users": users, "citygroups": citygroups, "about": about})
