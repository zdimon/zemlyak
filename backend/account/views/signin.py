from django.shortcuts import render
import requests

def signin(request):
    return render(request, 'account/signin.html')