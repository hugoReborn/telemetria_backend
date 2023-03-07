from django.contrib import admin
from .models import PositiveTorque, NegativeTorque, EngineTemperature
# Register your models here.


admin.site.register(PositiveTorque)
admin.site.register(NegativeTorque)
admin.site.register(EngineTemperature)
