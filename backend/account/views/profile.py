# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import UserProfile


def profile(request):
  
    user_profile = UserProfile.objects.get(publicname = 'Vitalii')
   
    
    return render(request,'account/profile.html',{"user_profile":user_profile });