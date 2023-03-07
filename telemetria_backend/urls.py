"""telemetria_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('battery/', include('applications.battery_signals.urls')),
    path('btms/', include('applications.btms_signals.urls')),
    path('bus/', include('applications.bus_signals.urls')),
    path('converter/', include('applications.converter_app.urls')),
    path('electrical/', include('applications.electrical_signals.urls')),
    path('engine/', include('applications.engine_signals.urls')),
    path('gps/', include('applications.gps_app.urls')),
    path('lenze/', include('applications.lenze_signals.urls')),
    path('other/', include('applications.other_signals.urls')),
    path('status/', include('applications.status_signals.urls')),
    path('technical/', include('applications.technical_info.urls')),

]
