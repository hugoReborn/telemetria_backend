from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class AcStatus(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    ac_status_value = models.FloatField('AC Status', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    ac_status = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.ac_status_value} - {self.bus}'


class Odometer(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    odometer_value = models.FloatField('Odometer', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    odometer = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.odometer_value} - {self.bus}'


class Pressure(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    pressure_value = models.FloatField('Pressure', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    pressure = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.pressure_value} - {self.bus}'


class Speed(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    speed_value = models.FloatField('Speed', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    speed = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.speed_value} - {self.bus}'


class ServiceCompressor(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    service_compressor_value = models.FloatField('Service Compressor', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    service_compressor = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.service_compressor_value} - {self.bus}'