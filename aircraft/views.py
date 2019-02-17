from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import AircraftSerializer, TestFlightTypeSerializer, FlightDataSerializer, FlightTypeSerializer
from .models import Aircraft, TestFlightType, FlightType, FlightData
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """去除 CSRF 检查"""

    def enforce_csrf(self, request):
        return


class AircraftViewSet(ModelViewSet):
    queryset = Aircraft.objects.all()  # 设置query集
    serializer_class = AircraftSerializer  # 指定序列化器


class TestFlightTypeViewSet(ModelViewSet):
    queryset = TestFlightType.objects.all()
    serializer_class = TestFlightTypeSerializer


class FlightTypeViewSet(ModelViewSet):
    queryset = FlightType.objects.all()
    serializer_class = FlightTypeSerializer


class FlightDataViewSet(ModelViewSet):
    queryset = FlightData.objects.all()
    serializer_class = FlightDataSerializer


def home(request):
    with open('templates/index.html', 'rb') as f:
        content = f.read()
    return HttpResponse(content)


def js(request, filename):
    with open('templates/js/{}'.format(filename), 'rb') as f:
        content = f.read()
    return HttpResponse(content=content,
                        content_type='application/javascript')


def css(request, filename):
    with open('templates/css/{}'.format(filename), 'rb') as f:
        content = f.read()
    return HttpResponse(content=content,
                        content_type='text/css')
