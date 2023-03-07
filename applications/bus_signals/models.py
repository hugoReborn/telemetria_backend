from django.db import models

# Create your models here.

from django.db import models

bus_serie_choices = (
    ('1', 'Queltehue'),
    ('2', 'Tricahue'),
    ('3', 'Retrofit'),
)


class Bus(models.Model):
    bus_name = models.CharField('Name', max_length=10, unique=True, blank=False)
    bus_sniffer = models.CharField('Sniffer', max_length=10, unique=True, blank=False)
    bus_plate_number = models.CharField('Plate Number', max_length=10, blank=False)
    bus_client = models.CharField('Client', max_length=10, blank=False)
    bus_serie = models.CharField('Serie', max_length=10, blank=False, choices=bus_serie_choices)
    bus_vin = models.CharField('VIN', max_length=20, blank=False)

    bus = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.bus_name} - {self.bus_sniffer} - {self.bus_plate_number} - {self.bus_client} - ' \
               f'{self.bus_serie} - {self.bus_vin}'
