from django.shortcuts import render
import requests
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from account.models import Country, City
from backend.settings import API_URL


def signin_only(request):
    
    return render(request, 'account/signin_only.html')