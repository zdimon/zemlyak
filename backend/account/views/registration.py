# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from account.serializers.registration import RegistrationRequestSerializer
from django.urls import reverse

from django.shortcuts import render
import requests
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from account.models import UserProfile, City
from django.contrib.auth import authenticate, login
from account.utils import add_city_group

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        publicname = request.POST['publicname']
        surename = request.POST['surename']
        source_city_alias = request.POST['source_city']
        source_city = City.objects.get(alias=source_city_alias)
        source_city = source_city
        target_city_alias = request.POST['target_city']
        target_city = City.objects.get(alias=target_city_alias)
        p = UserProfile()
        p.username = username
        p.set_password(password)
        p.publicname = publicname
        p.surename = surename
        p.source_city = source_city
        p.target_city = target_city
        p.save()
        add_city_group(source_city,target_city)
        login(request, p, backend='django.contrib.auth.backends.ModelBackend')
        messages.info(request, _('Добро пожаловать на сайт.'))  

        return redirect(reverse('city-detail', kwargs={'city':target_city_alias}))

class RegistrationView(APIView):
    '''

    User registration.

    __________________

    '''

    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        request_body = RegistrationRequestSerializer, \
        responses={200: RegistrationRequestSerializer} \
        )
    def post(self, request, format=None):
        obj = RegistrationRequestSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        profile = obj.save()
        return Response({'message': 'User %s has been created' % profile.username})