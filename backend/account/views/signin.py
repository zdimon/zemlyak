from django.shortcuts import render
import requests
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from account.models import Country, City
from backend.settings import API_URL


def signin(request):
    countries = Country.objects.all()
    def_country = Country.objects.get(alias='ukraine')
    cities = City.objects.filter(country=def_country)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, _('Добро пожаловать на сайт.'))   
            return redirect('/')         
        else:
            messages.warning(request, _('Ошибка. Неправильный логин или пароль'))    
    return render(request, 'account/signin.html', {"countries": countries, "cities": cities, "api_url": API_URL})