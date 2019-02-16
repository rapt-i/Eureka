from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(prefix='aircraft', viewset=views.AircraftViewSet)
router.register('testflighttype', viewset=views.TestFlightTypeViewSet)
router.register('flighttype', viewset=views.FlightTypeViewSet)
router.register('flightdata', viewset=views.FlightDataViewSet)
urlpatterns = [path('api', include(path('v1', include(router.urls)))),
               path('home', views.home, name='home'),
               path('js', views.js, 'name=js'),
               path('css', views.css, 'name=css'),
               ]
# http://url + api/v1/ + aircraft
