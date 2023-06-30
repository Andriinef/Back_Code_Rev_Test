"""
1. Annotate on Container query if it has a DeviceToContainer
(annotate true, false, or the id of the DeviceToContainer)
2. Annotate on Container query the imei or device_eui
from the DeviceToContainer.device for a Container.
1. Аннотировать запрос контейнера, если он имеет DeviceToContainer
(аннотировать true, false или идентификатор DeviceToContainer)
2. Аннотировать в контейнере запрос imei или device_eui
из DeviceToContainer.device для контейнера.
"""


from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.db import models


class MobileDevice(models.Model):
    imei = models.CharField(max_length=256)


class LorawanDevice(models.Model):
    device_eui = models.CharField(max_length=32)


class Container(models.Model):
    name = models.CharField(max_length=32)

    # Аннотация, указывающая на наличие DeviceToContainer у контейнера
    has_device_to_container = models.BooleanField(default=False)

    # Аннотация, указывающая imei или device_eui устройства
    # в DeviceToContainer для контейнера
    device_identifier = models.CharField(max_length=256, null=True, blank=True)


class DeviceToContainer(models.Model):
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    device = fields.GenericForeignKey()

    def save(self, *args, **kwargs):
        # Обновление аннотаций у контейнера при сохранении DeviceToContainer
        self.container.has_device_to_container = True

        # Проверка типа устройства и установка соответствующего идентификатора
        if isinstance(self.device, MobileDevice):
            self.container.device_identifier = self.device.imei
        elif isinstance(self.device, LorawanDevice):
            self.container.device_identifier = self.device.device_eui

        self.container.save()
        super().save(*args, **kwargs)
