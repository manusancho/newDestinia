__author__ = 'Manu'
import csv

from backend.apps.hotels.models import Airport


UPDATE_FILENAME = "hotels/airports.dat"
with open(UPDATE_FILENAME) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[4] is not "":
            try:
                _, created = Airport.objects.update_or_create(
                    id=row[0],
                    code=row[4],
                    name=row[1],
                    latitude=row[6],
                    longitude=row[7],
                )
            except Exception, e:
                print e
