from django.db import models
from applications.bus_signals.models import Bus

# Create your models here.

fusi_level_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class FusiMessage(models.Model):
    fusi_code = models.CharField('Fusi Code', max_length=10)
    fusi_description = models.CharField('Fusi Description', max_length=200)
    fusi_level = models.CharField('Fusi Level', max_length=5, choices=fusi_level_choices)

    fusi_message = models.Manager()

    def __str__(self):
        return f'{self.fusi_code} - {self.fusi_description} - {self.fusi_level}'


class BucketPaths(models.Model):
    path_sniffer = models.CharField('Path Sniffer', max_length=20)
    path_name = models.CharField('Path Name', max_length=100)
    path_creation = models.CharField('Path Creation', max_length=50)
    path_status = models.CharField('Path Status', max_length=5)

    bucket_paths = models.Manager()

    def __str__(self):
        return f'{self.path_sniffer} - {self.path_name} - {self.path_creation} - {self.path_status}'


class RemTechnician(models.Model):
    technician_name = models.CharField('Technician Name', max_length=50)
    technician_email = models.EmailField('Technician Email', max_length=50)
    technician_phone = models.CharField('Technician Phone', max_length=20)
    technician_position = models.CharField('Technician Position', max_length=10)
    technician_image = models.CharField('Technician Image', max_length=100)

    rem_technician = models.Manager()

    def __str__(self):
        return f'{self.technician_name} - {self.technician_email} - {self.technician_phone} -' \
               f' {self.technician_position} - {self.technician_image}'


class RemWorkOrder(models.Model):
    work_order_date = models.DateTimeField('Work Order', max_length=20)
    work_order_description = models.CharField('Work Order Description', max_length=500)
    work_order_failure_component = models.CharField('Work Order Failure Component', max_length=50)
    work_order_failure_component2 = models.CharField('Work Order Failure Component 2', max_length=50)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=False, null=False)
    rem_technician = models.ForeignKey(RemTechnician, on_delete=models.CASCADE, blank=False, null=False)

    rem_work_order = models.Manager()

    def __str__(self):
        return f'{self.work_order_date} - {self.work_order_description} - {self.work_order_failure_component} -' \
               f' {self.work_order_failure_component2} - {self.bus} - {self.rem_technician}'


class MarkVersion(models.Model):
    mark_version_mayor = models.CharField('Mark Version Mayor', max_length=5)
    mark_version_minor = models.CharField('Mark Version Minor', max_length=5)
    mark_version_revision = models.CharField('Mark Version Revision', max_length=5)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=False, null=False)

    mark_version = models.Manager()

    def __str__(self):
        return f'{self.mark_version_mayor} - {self.mark_version_minor} - {self.mark_version_revision} - {self.bus}'
