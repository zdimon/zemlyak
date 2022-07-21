from django_filters import FilterSet, NumberFilter, CharFilter
from account.models import City


class CityFilter(FilterSet):
    token = CharFilter()
    class Meta:
        model = City
        fields = ['country_alias']