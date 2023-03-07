from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class PositiveTorque(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    positive_torque_value = models.FloatField('Positive Torque', blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    positive_torque = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.positive_torque_value} - {self.bus}'


class NegativeTorque(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    negative_torque_value = models.FloatField('Negative Torque', blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    negative_torque = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.negative_torque_value} - {self.bus}'


class EngineTemperature(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    engine_temperature_value = models.FloatField('Engine Temperature', blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    engine_temperature = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.engine_temperature_value} - {self.bus}'

