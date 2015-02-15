from datetime import datetime

from django.db import models
from django.contrib import admin

class Provider(models.Model):
    machine_name = models.CharField(
        'Machine name',
        max_length=10,
        )
    name = models.CharField(
        'Name',
        max_length=60,
        )
    contactTelephone = models.CharField(
        'Contact telephone',
         max_length=255,
        blank=True,
        null= True
        )
    contactEmail = models.EmailField(
        'Contact email',
        max_length=70,
        blank=True,
        null= True,
        )
    enabled = models.BooleanField(
        'Enabled',
        help_text='Enable this provider to import data from it',
        default=False,
        )
    created = models.DateField(
        'Creation date',
        auto_now=False,
        auto_now_add=True,
        editable=False,
        default=datetime.now(),
        )
    updated = models.DateField(
        'Updated date',
        auto_now=True,
        auto_now_add=False,
        editable=False,
        default=datetime.now(),
        )
    autoUpdateEnabled = models.BooleanField(
        'Update automatically',
        default=False,
        )
    autoUpdateHour = models.SmallIntegerField(
        'Update hour',
        blank=True,
        null= True,
        )
    autoUpdateMin = models.SmallIntegerField(
        'Update minutes',
        blank=True,
        null= True,
        )
    autoUpdateExecTime = models.IntegerField(
        'Las execution duration',
         editable=False,
         null= True,
        )
    keepInboundFile = models.BooleanField(
        'Keep downloaded files after import',
        default=True,
        )
    keepInboundFileDays = models.SmallIntegerField(
        'Days to keep import files',
        blank=True,
        default=7,
        )

    def update(self):
        """
        Retrieve information from
        :return:
        """
        raise NotImplementedError("Please Implement update() method in this Provider")

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ['name']

    class Admin:
        pass

class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'enabled',
        'autoUpdateEnabled',
        'autoUpdateHour','autoUpdateEnabled',
        'keepInboundFile', 'keepInboundFileDays',
    )
    fieldsets = (
        (None, {
            'classes': ('wide','extrapretty'),
            'fields': ('machine_name','name', 'enabled')
        }),
        ('Contact', {
            'classes': ('wide',),
            'fields': ('contactTelephone','contactEmail',)
        }),
        ('Update', {
            'classes': ('wide',),
            'fields': ('autoUpdateEnabled', ('autoUpdateHour', 'autoUpdateMin'))
        }),
        ('Files', {
            'classes': ('wide',),
            'fields': ('keepInboundFile', 'keepInboundFileDays')
        }),
    )

class BoardTypeMap():
    provider = models.OneToOneField(Provider)
    providerBoardType = models.CharField(max_length=3)
    internalBoardType = models.OneToOneField('offers.BoardType')


class RoomTypeMap():
    provider = models.OneToOneField(Provider)
    providerRoomType = models.CharField(max_length=4)
    internalRoomType = models.OneToOneField('offers.RoomType')