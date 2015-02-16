from django.db import models
from datetime import datetime


# Auxiliary classes
class Airport(models.Model):
    code_iata = models.CharField(
        max_length=3,
        blank=True
        )
    code_icao = models.CharField(
        max_length=4,
        blank=True,
        )
    name = models.CharField(
        max_length=100
    )
    latitude = models.FloatField('Latitude',
                                 blank=True,
                                 null=True)
    longitude = models.FloatField('Longitude',
                                  blank=True,
                                  null=True)


    def __unicode__(self):
        return u'%s-%s' % (self.code_iata, self.name)

    def __str__(self):
        return '%s-%s' % (self.code_iata, self.name)

    class Meta:
        ordering = ['code_iata']

    class Admin:
        pass


class Continent(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name_es = models.CharField(max_length=20, blank=True)
    name_en = models.CharField(max_length=20, blank=True)
    name_de = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return u"%s" % (self.__get_name())

    def __str__(self):
        return '%s' % (self.__get_name())

    def __get_name(self):
        if self.name_es:
            return self.name_es
        elif self.name_en:
            return self.name_en
        elif self.name_de:
            return self.name_de
        else:
            return ''

    class Meta:
        ordering = ['code']

    class Admin:
        pass


class Country(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name_es = models.CharField(max_length=45, blank=True)
    name_en = models.CharField(max_length=45, blank=True)
    name_de = models.CharField(max_length=45, blank=True)
    continent = models.ForeignKey(Continent, null=True)

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.__get_name())

    def __str__(self):
        return '%s-%s' % (self.code, self.__get_name())

    def __get_name(self):
        if self.name_es:
            return self.name_es
        elif self.name_en:
            return self.name_en
        elif self.name_de:
            return self.name_de
        else:
            return ''

    class Meta:
        ordering = ['code']
        verbose_name_plural = "Countries"

    class Admin:
        pass


class Destination(models.Model):
    destination_id = models.PositiveIntegerField()
    name_es = models.CharField(max_length=100, blank=True)
    name_en = models.CharField(max_length=100, blank=True)
    name_de = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country, null=True)

    def __unicode__(self):
        return u"%s" % self.__get_name()

    def __str__(self):
        return '%s' % self.__get_name()

    def __get_name(self):
        if self.name_es:
            return self.name_es
        elif self.name_en:
            return self.name_en
        elif self.name_de:
            return self.name_de
        else:
            return ''


    class Meta:
        ordering = ['country', 'name_es']

    class Admin:
        pass


class City(models.Model):
    city_id = models.PositiveIntegerField()
    name_es = models.CharField(
        max_length=100,
        blank=True
    )
    name_en = models.CharField(
        max_length=100,
        blank=True
    )
    name_de = models.CharField(
        max_length=100,
        blank=True
    )
    destination = models.ForeignKey(
        Destination,
        null=True
    )
    airports = models.ManyToManyField(
        Airport,
        null=True
    )

    def __unicode__(self):
        return u"%s" % self.__get_name()

    def __str__(self):
        return '%s' % (self.__get_name())

    def __get_name(self):
        if self.name_es:
            return self.name_es
        elif self.name_en:
            return self.name_en
        elif self.name_de:
            return self.name_de
        else:
            return ''


    class Meta:
        ordering = ['name_es']
        verbose_name_plural = "Cities"

    class Admin:
        pass


class Hotel(models.Model):
    name = models.CharField(
        max_length=200,
        )
    category = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        )
    latitude = models.FloatField(
        blank=True,
        null=True,
        )
    longitude = models.FloatField(
        blank=True,
        null=True,
        )
    city = models.ForeignKey(
        City,
        null=True,
    )
    giata_id = models.PositiveIntegerField(
        'Giata ID',
        unique=True,
        )
    buchungcode = models.CharField(
        max_length=8,
        null=True,
        )
    description_es = models.TextField(
        'Descr. ES',
        blank=True,
        null=True,
        )
    enabled = models.BooleanField(
        default=True,
        )
    created = models.DateField(
        auto_now=False,
        auto_now_add=True,
        editable=False,
        default=datetime.now(),
        )
    updated = models.DateField(
        auto_now=True,
        auto_now_add=False,
        editable=False,
        default=datetime.now(),
        )

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        list_filter = ('name', 'category', 'city')
        ordering = ('name',)
        search_fields = ('title', 'giataid', 'buchungcode', 'city', 'description_es')
