from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class PtcVoltage(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    ptc_voltage_value = models.FloatField('PTC Voltage', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    ptc_voltage = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.ptc_voltage_value}'


class Isolation(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    isolation_value = models.FloatField('Isolation', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    isolation = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.isolation_value} - {self.bus}'

# Create your models here.
