from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.


class FusiCode(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    fusi_code = models.CharField('Fusi Code', max_length=10, blank=True, null=True)
    fusi_state = models.CharField('Fusi State', max_length=10, blank=True, null=True)
    fusi_comment = models.CharField('Fusi Comment', max_length=300, blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    fusi = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.fusi_code} - {self.fusi_state} - {self.fusi_comment} - {self.bus}'


class ChargeStatus(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    charge_status_value = models.FloatField('Charge Status Value', blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    charge_status = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.charge_status_value} - {self.bus}'


class Gear(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    gear_value = models.CharField('Gear Value', max_length=10, blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    gear = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.gear_value} - {self.bus}'


bus_state_choices = (
    ('1', 'Activo'),
    ('2', 'Fuera de Servicio')
)


class BusState(models.Model):
    """This Model has an auto_now_add attribute, which means that the field will be automatically set to now when
    the object is first created."""
    TimeStamp = models.DateTimeField('TimeStamp', auto_now_add=True, blank=True, null=True)
    bus_state_value = models.CharField('Bus State Value', choices=bus_state_choices, max_length=10, blank=True,
                                       null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    bus_state = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.bus_state_value} - {self.bus}'


class BrakePedal(models.Model):
    TimeStamp = models.DateTimeField('TimeStamp', blank=True, null=True)
    brake_pedal_value = models.CharField('Brake Pedal Value', max_length=10, blank=True, null=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    brake_pedal = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.brake_pedal_value} - {self.bus}'

