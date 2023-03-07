from django.db import models
from applications.bus_signals.models import Bus


# Create your models here.

class Battery24Volts(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_24_volts_value = models.FloatField('Battery 24 Volts', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_24_volts = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_24_volts_value} - {self.bus}'


class Soc(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    soc_value = models.FloatField('State of Charge', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    soc = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.soc_value} - {self.bus}'


class BatteryPackTemperature(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_temperature_value = models.FloatField('Battery Pack Temperature', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_temperature = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_temperature_value} - {self.bus}'


class BatteryPackMaxTemperature(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_max_temperature_value = models.FloatField('Battery Pack Max Temperature', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_max_temperature = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_max_temperature_value} - {self.bus}'


class BatteryPackMinTemperature(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_min_temperature_value = models.FloatField('Battery Pack Min Temperature', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_min_temperature = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_min_temperature_value} - {self.bus}'


class BatteryHealth(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_health_value = models.FloatField('Battery Health', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_health = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_health_value} - {self.bus}'


class BatteryPackVoltage(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_voltage_value = models.FloatField('Battery Pack Voltage', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_voltage = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_voltage_value} - {self.bus}'


class BatteryPackCurrent(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_current_value = models.FloatField('Battery Pack Current', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_current = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_current_value} - {self.bus}'


class BatteryPackCellMaxVoltage(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_cell_max_voltage_value = models.FloatField('Battery Pack Cell Max Voltage', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_cell_max_voltage = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_cell_max_voltage_value} - {self.bus}'


class BatteryPackCellMinVoltage(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_cell_min_voltage_value = models.FloatField('Battery Pack Cell Min Voltage', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_cell_min_voltage = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_cell_min_voltage_value} - {self.bus}'


class BatteryPackAvgVoltageCell(models.Model):
    TimeStamp = models.DateTimeField('Timestamp', null=True, blank=True)
    battery_pack_avg_voltage_cell_value = models.FloatField('Battery Pack Avg Voltage Cell', null=True, blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    battery_pack_avg_voltage_cell = models.Manager()

    def __str__(self):
        return f'{self.TimeStamp} - {self.battery_pack_avg_voltage_cell_value} - {self.bus}'
