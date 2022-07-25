# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import CityGroup, City


def city_detail(request, city):
    city = City.objects.get(alias=city)
    return render(request,'account/city_detail.html',{"city": city});