import django_filters
from .models import FlightData


class FlightDataFilter(django_filters.rest_framework.FilterSet):
    """
    FlightData过滤器
    """
    flight_type = django_filters.NumberFilter(field_name='flight_type')

    class Meta:
        model = FlightData
        fields = ['flight_type']