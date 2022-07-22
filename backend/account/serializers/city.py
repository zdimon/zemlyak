# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from account.models import City


class GetCityRequestSerializer(serializers.Serializer):
    country = serializers.CharField()

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id',
            'alias',
            'name'
        ]    