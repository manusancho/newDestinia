from django.db import models


# Auxiliary classes
class RoomType(models.Model):
    code = models.CharField(max_length=4)
    nameEs = models.CharField(max_length=30)
    nameEn = models.CharField(max_length=30)
    nameDe = models.CharField(max_length=30)
    minPax = models.SmallIntegerField()
    maxPax = models.SmallIntegerField()
    minAdults = models.SmallIntegerField()
    maxAdults = models.SmallIntegerField()
    minChildren = models.SmallIntegerField()
    maxChildren = models.SmallIntegerField()

    def __str__(self):
        return '%s-%s' % (self.code, self.name_es)

    class Meta:
        ordering = ['code']

    class Admin:
        pass


class BoardType(models.Model):
    code = models.CharField(max_length=3)
    nameEs = models.CharField(max_length=30)
    nameEn = models.CharField(max_length=30)
    nameDe = models.CharField(max_length=30)

    def __str__(self):
        return '%s-%s' % (self.code, self.name_es)

    class Meta:
        ordering = ['code']

    class Admin:
        pass


class Offer(models.Model):
    hotel = models.ForeignKey('hotels.Hotel')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    roomTypes = models.ManyToManyField('offers.RoomType')
    boardTypes = models.ManyToManyField('offers.BoardType')
    validFrom = models.DateField()
    validTo = models.DateField()
    priority = models.SmallIntegerField(default=1)
    provider = models.ForeignKey('providers.Provider')

    class Meta:
        order_with_respect_to = 'provider'

    class Admin:
        pass