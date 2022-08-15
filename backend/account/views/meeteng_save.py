# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import UserProfile


def meeteng_save(request):
    if request.method == 'POST':
        message = request.post.get['message']
        cafe = request.post.get['cafe']
    return render(request,'account/mycontacts.html',{});