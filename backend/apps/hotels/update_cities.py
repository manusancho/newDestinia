__author__ = 'Manu'

import csv
import codecs

from backend.apps.hotels.models import *


UPDATE_FILENAME = "hotels/giatadaten2.csv"
with codecs.open(UPDATE_FILENAME) as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print row
        giataid = row[0]
        hotel_name = row[1].decode('latin-1')
        country_code = row[2]
        country_name = row[3].decode('latin-1')
        destination_id = row[4]
        destination_name = row[5].decode('latin-1')
        city_id = row[6]
        city_name = row[7].decode('latin-1')
        country, created = Country.objects.update_or_create(
            code=country_code,
            name_de=country_name,
        )
        destination, created = Destination.objects.update_or_create(
            id=destination_id,
            name_de=destination_name,
            country=country,
        )
        city, created = City.objects.update_or_create(
            id=city_id,
            name_de=city_name,
            destination=destination,
        )
        hotel, created = Hotel.objects.update_or_create(
            giataid=giataid,
            name=hotel_name,
            city=city,
        )