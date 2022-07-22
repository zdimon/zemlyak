from django.urls import path, include
from account.views.registration import RegistrationView
from account.views.user_list import UserListView
from account.views.login import LoginView, LogoutView
from account.views.init import InitView
from .views import signin, registration
from .views.get_city import GetCityView
from .views.group_detail import city_group_detail


urlpatterns = [ 
    path('registration',RegistrationView.as_view()),
    path('user_list',UserListView.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogoutView.as_view()),
    path('init',InitView.as_view()),
    path('signin',signin, name='signin'),
    path('user-registration',registration, name='user-registration'),
    path('get_city',GetCityView.as_view()),
    path('city/group/detail/<slug:source_city>/<slug:target_city>',city_group_detail, name="city-group-detail"),
]