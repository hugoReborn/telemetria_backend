from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class LenzeCurrent(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    lenze_current_value = models.FloatField('Lenze Current', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    lenze_current = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.lenze_current_value} - {self.bus}'


class LenzeEngineSpeed(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    lenze_engine_speed_value = models.FloatField('Lenze Engine Speed', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    lenze_engine_speed = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.lenze_engine_speed_value} - {self.bus}'

