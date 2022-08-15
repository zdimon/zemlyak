from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from account.models import City, Country
from account.serializers.city import GetCityRequestSerializer, CitySerializer
from account.filters.city import CityFilter
from rest_framework import generics

class GetCityView(generics.ListAPIView):
    '''
    
    Get cityes.


    '''
    serializer_class = CitySerializer
    filterset_class = CityFilter
    queryset = City.objects.all().order_by('name_ru')
    pagination_class = None
