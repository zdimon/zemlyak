# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import CityGroup, City


def city_group_detail(request, source_city, target_city):
    scity = City.objects.get(name_en=source_city)
    tcity = City.objects.get(name_en=target_city)
    group = CityGroup.objects.get(target=tcity, source=scity)
    return render(request,'account/group_detail.html',{"group": group});