# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class SearchCityView(APIView):
    '''

    Search city.

    __________________

    '''

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response({"status": "OK"})
 