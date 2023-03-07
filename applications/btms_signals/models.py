from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class BtmsStatus(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    btms_status_value = models.FloatField('BTMS Status', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    btms_status = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.btms_status_value} - {self.bus}'


class BtmsPowerRequest(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    btms_power_request_value = models.FloatField('BTMS Power Request', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    btms_power_request = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.btms_power_request_value} - {self.bus}'


class BtmsFaultCode(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    btms_fault_code_value = models.FloatField('BTMS Fault Code', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    btms_fault_code = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.btms_fault_code_value} - {self.bus}'


class BtmsTemperature(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    btms_temperature_value = models.FloatField('BTMS Temperature', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    btms_temperature = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.btms_temperature_value} - {self.bus}'


class BtmsActive(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    btms_active_value = models.FloatField('BTMS Active', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    btms_active = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.btms_active_value} - {self.bus}'
# Create your models here.

