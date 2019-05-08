from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(prefix='aircraft', viewset=views.AircraftViewSet)
router.register('tftype', viewset=views.TestFlightTypeViewSet)
router.register('flighttype', viewset=views.FlightTypeViewSet)
router.register('flightdata', viewset=views.FlightDataViewSet)
api_v1 = [path('v1/', include(router.urls))]
urlpatterns = [path('api/', include(api_v1)),
               path('', views.home, name='home'),
               path('js/<str:filename>', views.js, name='js'),
               path('css/<str:filename>', views.css, name='css'),
               ]
# http://url + api/v1/ + aircraft
