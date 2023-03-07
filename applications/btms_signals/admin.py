from django.contrib import admin
from . models import (BtmsStatus, BtmsPowerRequest,
                      BtmsFaultCode, BtmsTemperature, BtmsActive)


# Register your models here.

admin.site.register(BtmsStatus)
admin.site.register(BtmsPowerRequest)
admin.site.register(BtmsFaultCode)
admin.site.register(BtmsTemperature)
admin.site.register(BtmsActive)