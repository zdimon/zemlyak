from django.urls import path, include
from .index.views import main_page, homepage
from .views import city_group

urlpatterns = [ 
    path('',main_page),
    path('city/group/<slug:city>',city_group, name="city-group"),
]