from django.contrib import admin
from .models import AcStatus, Odometer, Pressure, Speed, ServiceCompressor
# Register your models here.


admin.site.register(AcStatus)
admin.site.register(Odometer)
admin.site.register(Pressure)
admin.site.register(Speed)
admin.site.register(ServiceCompressor)
