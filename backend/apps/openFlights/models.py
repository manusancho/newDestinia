# -- coding: utf-8 --
import os, csv

from solo.models import SingletonModel

from backend.utils import download

from backend.apps.siteConfiguration.models import *
from backend.apps.hotels.models import *



class OpenFlights(SingletonModel):
    filename_uri = models.CharField(
        'Airports CSV',
        help_text="URL to download airports.dat file from OpenFlights website",
        default='https://sourceforge.net/p/openflights/code/HEAD/tree/openflights/data/airports.dat?format=raw',
        max_length=255,
        )
    filename_uri_enable = models.BooleanField(
        'Enable airports update',
        default=True,
        )
    download_folder = models.CharField(
        'Download folder name',
        help_text="Name of the folder inside files folder to store OpenFlights downloaded files",
        default='openFlights',
        max_length=255,
        )


    def __unicode__(self):
        return u"OpenFlights configuration"

    class Meta:
        verbose_name = "OpenFlights configuration"


    # Private methods
    def __download_file(self):

        return download.http_file(
            self.filename_uri,
            self.__get_download_path(),
            'airports.dat',
        )

    def __get_download_path(self):

        # Get site configuration
        siteConfiguration = SiteConfiguration.get_solo()

        return os.path.abspath(
            os.path.join(
                siteConfiguration.filespath,
                self.download_folder
            )
        )

    def __get_local_uri(self):

        # Get site configuration
        siteConfiguration = SiteConfiguration.get_solo()

        return os.path.abspath(
            os.path.join(
                siteConfiguration.filespath,
                self.download_folder,
                'airports.dat',
            )
        )

    def __get_filename(self):

        return os.path.basename(self.filename_uri)


    # Public methods
    def flush_airports(self):

        Airport.objects.all().delete()
        print "Airports database cleared!"

    def update_airports(self):

        if self.filename_uri_enable:
            result = self.__download_file()
            if result is not True:
                # TODO: log error
                return result

            result = self.parse_airports()
            if result is not True:
                # TODO: log error
                return result

        return True


    def parse_airports(self):

        lines = created_airports = 0

        csv_filepath = self.__get_local_uri()
        print "Parsing %s" % csv_filepath

        try:
            reader = csv.reader(
                open(csv_filepath)
            )
        except Exception, e:
            return "Error parsing %s. %s" (csv_filepath,e)

        for row in reader:
            #print row
            if row[4] is "":
                continue

            airport_id = row[0]
            airport_name = row[1].decode('latin-1')
            airport_iata = row[4]
            airport_icao = row[5]
            airport_latitude = row[6]
            airport_longitude = row[7]

            try:
                airport, created = Airport.objects.update_or_create(
                    id=airport_id,
                    name=airport_name,
                    code_iata=airport_iata,
                    code_icao=airport_icao,
                    latitude=airport_latitude,
                    longitude=airport_longitude,
                    )
                if created:
                    print "Added airport %s-%s" % (airport_iata, airport_name)
                    created_airports+=1

            except Exception, e:
                print e

            lines += 1

        print "Processed %s lines from %s. Created %s airports" %\
            (lines, csv_filepath, created_airports)

        return True