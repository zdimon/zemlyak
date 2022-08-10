# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import City

class SearchCityView(APIView):
    '''

    Search city.

    __________________

    '''

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        key = request.GET.get("q",None)
        cities = []
        if key:
            citiesq = City.objects.filter(search__icontains=key)[0:10]
        for city in citiesq:
            cities.append(
                {
                    "name": f'{city.name} {city.country}',
                    "alias": city.alias
                }
            )

        return Response(cities)
 