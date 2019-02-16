from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Aircraft)
admin.site.register(models.TestFlightType)
admin.site.register(models.FlightType)
admin.site.register(models.FlightData)
