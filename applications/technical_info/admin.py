from django.contrib import admin
from .models import FusiMessage, BucketPaths, RemTechnician, RemWorkOrder, MarkVersion
# Register your models here.

admin.site.register(FusiMessage)
admin.site.register(BucketPaths)
admin.site.register(RemTechnician)
admin.site.register(RemWorkOrder)
admin.site.register(MarkVersion)

