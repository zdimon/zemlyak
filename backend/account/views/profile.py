# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import UserProfile


def profile(request):
    # user_id = request.user.useraccount
    # user_profile = UserProfile.objects.get(publicname = 'Vitalii')
    # print (user_id)
    # user_profile = UserProfile.objects.get(id = user_id)
    
    user_profile = request.user.userprofile
    print(user_profile)

    return render(request,'account/profile.html',{"user_profile":user_profile });