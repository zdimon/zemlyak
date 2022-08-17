# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib import messages
from account.models import UserProfile, Cafe, Meeting
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def meeteng_save(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        cafe_id = request.POST.get('cafe')
        cafe = Cafe.objects.get(pk=cafe_id)
        m = Meeting()
        m.user = request.user.userprofile
        m.cafe = cafe
        m.message = message
        m.save()
        messages.info(request, _('Спасибо. Ваша заявка сохранена и будет отослана вашим землякам в этом городе.')) 
        return redirect(reverse('city-detail', kwargs={'city':cafe.city.alias}))

    return render(request,'account/mycontacts.html',{});