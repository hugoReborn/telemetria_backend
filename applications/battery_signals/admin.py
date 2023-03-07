from django.contrib import admin
from .models import (Battery24Volts, Soc, BatteryPackTemperature,
                     BatteryPackMaxTemperature, BatteryPackMinTemperature,
                     BatteryHealth, BatteryPackVoltage, BatteryPackCurrent,
                     BatteryPackCellMaxVoltage, BatteryPackCellMinVoltage,
                     BatteryPackAvgVoltageCell)

# Register your models here.

admin.site.register(Battery24Volts)
admin.site.register(Soc)
admin.site.register(BatteryPackTemperature)
admin.site.register(BatteryPackMaxTemperature)
admin.site.register(BatteryPackMinTemperature)
admin.site.register(BatteryHealth)
admin.site.register(BatteryPackVoltage)
admin.site.register(BatteryPackCurrent)
admin.site.register(BatteryPackCellMaxVoltage)
admin.site.register(BatteryPackCellMinVoltage)
admin.site.register(BatteryPackAvgVoltageCell)
