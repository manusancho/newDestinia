# -- coding: utf-8 --

import os, csv

from solo.models import SingletonModel

from backend.utils import download
from backend.apps.siteConfiguration.models import *
from backend.apps.hotels.models import *


class Giata(SingletonModel):
    ftp_server = models.CharField(
        'FTP Server',
        max_length=255,
        default='ftp1.giata-web.de',
        )
    ftp_user = models.CharField(
        'Username',
        max_length=255,
        )
    ftp_password = models.CharField(
        'Password',
        max_length=255,
    )
    filename_uri_countries = models.CharField(
        'Countries CSV',
        default='laenderinfo/laenderinfo.csv',
        help_text="It can be a path like 'laenderinfo/laenderinfo.csv'",
        max_length=255,
    )
    filename_uri_countries_enable = models.BooleanField(
        'Enable countries CSV',
        default=True,
        )
    filename_uri_destinations = models.CharField(
        'Destinations CSV',
        default='laenderinfo/destinations.csv',
        help_text="It can be a path like 'laenderinfo/destinations.csv'",
        max_length=255,
    )
    filename_uri_destinations_enable = models.BooleanField(
        'Enable destinations CSV',
        default=True,
        )
    filename_uri_cities = models.CharField(
        'Cities CSV',
        default='laenderinfo/cities.csv',
        help_text="It can be a path like 'laenderinfo/cities.csv'",
        max_length=255,
    )
    filename_uri_cities_enable = models.BooleanField(
        'Enable cities CSV',
        default=True,
        )
    filename_uri_hotels = models.CharField(
        'Hotels CSV',
        default='giatadaten/giatadaten.csv',
        help_text="It can be a path like 'giatadaten/giatadaten.csv'",
        max_length=255,
    )
    filename_uri_hotels_enable = models.BooleanField(
        'Enable hotels CSV',
        default=True,
        )
    download_folder = models.CharField(
        'Download folder name',
        help_text="Name of the folder inside files folder to store giata downloaded files",
        default='giata',
        max_length=255,
    )
    updateHotels = models.BooleanField(
        'Update hotels',
        help_text="Add new hotels to database",
        default=True,
        )
    updateDestinations = models.BooleanField(
        'Update destinations',
        help_text="Add new destinations to database",
        default=True,
        )
    updateCountries = models.BooleanField(
        'Update hotels',
        help_text="Add new countries to database",
        default=True,
        )
    updateCities = models.BooleanField(
        'Update cities',
        help_text="Add new cities to database",
        default=True,
        )


    def __unicode__(self):
        return u"Giata configuration"

    class Meta:
        verbose_name = "Giata configuration"


    # Private methods
    def __download_file(self, type):

        return download.ftp_file(
            self.ftp_server,
            self.ftp_user,
            self.ftp_password,
            self.__get_remote_uri(type),
            self.__get_download_path(),
            )

    def __get_remote_uri(self, type):

        if type is 'countries':
            filename_uri = self.filename_uri_countries
        elif type is 'destinations':
            filename_uri = self.filename_uri_destinations
        elif type is 'cities':
            filename_uri = self.filename_uri_cities
        else: # 'hotels' or other
            filename_uri = self.filename_uri_hotels

        return filename_uri

    def __get_download_path(self):

        # Get site configuration
        siteConfiguration = SiteConfiguration.get_solo()

        return os.path.abspath(
            os.path.join(
                siteConfiguration.filespath,
                self.download_folder
            )
        )

    def __get_local_uri(self, type):

        # Get site configuration
        siteConfiguration = SiteConfiguration.get_solo()

        return os.path.abspath(
            os.path.join(
                siteConfiguration.filespath,
                self.download_folder,
                self.__get_filename(type),
            )
        )

    def __get_filename(self, type):

        return os.path.basename(self.__get_remote_uri(type))


    # Public methods
    def update_countries(self):
        if self.filename_uri_countries_enable:
            result = self.__download_file('countries')
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_countries()
            if result is not True:
                # TODO: log error
                return result
        return True

    def update_destinations(self):
        if self.filename_uri_destinations_enable:
            result = self.__download_file('destinations')
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_destinations()
            if result is not True:
                # TODO: log error
                return result
        return True

    def update_cities(self):
        if self.filename_uri_cities_enable:
            result = self.__download_file('cities')
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_cities()
            if result is not True:
                # TODO: log error
                return result
        return True

    def update_hotels(self):
        if self.filename_uri_hotels_enable:
            result = self.__download_file('hotels')
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_hotels()
            if result is not True:
                # TODO: log error
                return result
        return True

    def update_airports(self):
        """
        if self.filename_uri_hotels_enable:
            result = self.__download_file(https://sourceforge.net/p/openflights/code/HEAD/tree/openflights/data/airports.dat?format=raw)
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_hotels()
            if result is not True:
                # TODO: log error
                return result
        """
        return True


    def parse_hotels(self):

        lines = created_countries \
            = created_destinations \
            = created_cities \
            = created_hotels = 0

        csv_filepath = self.__get_local_uri('hotels')
        reader = csv.reader(
            open(csv_filepath),
            delimiter=';',
            skipinitialspace=True,
        )

        next(reader, None) # skip header

        for row in reader:

            giata_id = row[0]
            hotelname = row[1].decode('cp1252')
            country_code = row[2]
            country_name = row[3].decode('cp1252')
            destination_id = row[4] # not used
            destination_name = row[5].decode('cp1252')
            city_id = row[6] # not used
            city_name = row[7].decode('cp1252')

            try:
                country, created = Country.objects.update_or_create(
                    code=country_code,
                    name_de=country_name,
                )
                if created:
                    print "Added country %s" % country_name
                    created_countries += 1

            except Exception, e:
                print e

            try:
                destination, created = Destination.objects.update_or_create(
                    destination_id=destination_id,
                    name_de=destination_name,
                    country=country,
                )
                if created:
                    print "Added destination %s" % destination_name
                    created_destinations+=1

            except Exception, e:
                print e


            try:
                city, created = City.objects.update_or_create(
                    city_id=city_id,
                    name_de=city_name,
                    destination=destination,
                )
                if created:
                    #print "Added city %s" % city_name
                    created_cities+=1

            except Exception, e:
                print e


            try:
                hotel, created = Hotel.objects.update_or_create(
                    name=hotelname,
                    giata_id=giata_id,
                    city=city,
                )
                if created:
                    #print "Added hotel %s with giataid=%s" % (city_name, giata_id)
                    created_hotels+=1

            except Exception, e:
                print e

            lines += 1

        print "Processed %s lines from %s. Created %s countries, %s destinations, %s cities and %s hotels" %\
            (lines, csv_filepath, created_countries, created_destinations, created_cities, created_hotels)

        return True

    def parse_destinations(self):

        lines = created_countries \
            = created_destinations = 0

        csv_filepath = self.__get_local_uri('destinations')
        reader = csv.reader(
            open(csv_filepath),
            delimiter=';',
            skipinitialspace=True,
        )

        next(reader, None) # skip header

        for row in reader:

            destination_id = row[0] # not used
            destination_name = row[1].decode('cp1252')
            country_code = row[2]

            try:
                country, created = Country.objects.update_or_create(
                    code=country_code,
                )
                if created:
                    print "Added country %s" % country_name
                    created_countries += 1

            except Exception, e:
                print e

            try:
                destination, created = Destination.objects.update_or_create(
                    destination_id=destination_id,
                    name_de=destination_name,
                    country=country,
                )
                if created:
                    print "Added destination %s" % destination_name
                    created_destinations+=1

            except Exception, e:
                print e

            lines += 1

        print "Processed %s lines from %s. Created %s countries and %s destinations" %\
            (lines, csv_filepath, created_countries, created_destinations)

        return True

    def parse_cities(self):

        lines = created_destinations \
            = created_cities = 0

        csv_filepath = self.__get_local_uri('cities')
        reader = csv.reader(
            open(csv_filepath),
            delimiter=';',
            skipinitialspace=True,
        )

        next(reader, None) # skip header

        for row in reader:

            city_id = row[0]
            city_name = row[1]
            destination_id = row[2]

            try:
                destination, created = Destination.objects.update_or_create(
                    destination_id=destination_id,
                )
                if created:
                    print "Added destination with id %s" % destination_id
                    created_destinations+=1

            except Exception, e:
                print e

            try:
                city, created = City.objects.update_or_create(
                    city_id=city_id,
                )
                if created:
                    print "Added city %s" % city_name
                    created_cities += 1

            except Exception, e:
                print e


            lines += 1

        print "Processed %s lines from %s. Created %s destinations and %s cities" %\
            (lines, csv_filepath, created_destinations, created_cities)

        return True

    def parse_countries(self):

        lines = created_countries \
            = created_destinations \
            = created_cities \
            = created_airports = 0

        csv_filepath = self.__get_local_uri('countries')
        reader = csv.reader(
            open(csv_filepath),
            delimiter=';',
            skipinitialspace=True,
        )

        next(reader, None) # skip header

        for row in reader:

            city_id = row[0]
            city_name = row[1].decode('cp1252')
            destination_id = row[2] # not used
            destination_name = row[3].decode('cp1252')
            airport_codes = row[4].split(" ")
            country_code = row[5]
            country_name = row[6].decode('cp1252')

            try:
                country, created = Country.objects.update_or_create(
                    code=country_code,
                    name_de=country_name,
                )
                if created:
                    print "Added country %s" % country_name
                    created_countries += 1

            except Exception, e:
                print e

            try:
                destination, created = Destination.objects.update_or_create(
                    destination_id=destination_id,
                    name_de=destination_name,
                    country=country,
                )
                if created:
                    print "Added destination %s" % destination_name
                    created_destinations+=1

            except Exception, e:
                print e

            try:
                city, created = City.objects.update_or_create(
                    city_id=city_id,
                    name_de=city_name
                )
                if created:
                    #print "Added city %s" % city_name
                    created_cities+=1

            except Exception, e:
                print e

            for airport_code in airport_codes:

                try:
                    airport, created = City.objects.get_or_create(
                        code=airport_code,
                    )
                    if created:
                        #print "Added airport %s" % airport_code
                        created_airports+=1

                    city.airports.add(airport)

                except Exception, e:
                    print e

            lines += 1

        print "Processed %s lines from %s. Created %s countries, %s destinations, %s cities and %s airports" %\
            (lines, csv_filepath, created_countries, created_destinations, created_cities, created_airports)

        return True