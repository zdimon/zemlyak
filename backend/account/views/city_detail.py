# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import CityGroup, City, Cafe, UserProfile
from django.contrib.auth.decorators import login_required


def city_detail(request, city):
    
    city = City.objects.get(alias=city)
    cafes = Cafe.objects.filter(city=city)
    if request.user.is_authenticated:
        mycity = request.user.userprofile.source_city
        users = UserProfile.objects.filter(source_city=mycity, target_city=city)
    else:
        users = UserProfile.objects.filter(target_city=city)[0:10]       
    return render(request,'account/city_detail.html',{"city": city, "cafes": cafes, "users": users});