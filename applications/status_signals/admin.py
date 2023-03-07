from django.contrib import admin
from .models import FusiCode, ChargeStatus, Gear, BusState, BrakePedal
# Register your models here.


admin.site.register(FusiCode)
admin.site.register(ChargeStatus)
admin.site.register(Gear)
admin.site.register(BusState)
admin.site.register(BrakePedal)
