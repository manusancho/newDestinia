from time import sleep
from django.http import HttpResponse

from backend.apps.openFlights.models import *


def update_airports(request):

    flush = (request.GET.get('flush') is 'True' or request.GET.get('flush') is 'true')
    openFlights = OpenFlights.get_solo()

    if flush:
        openFlights.flush_airports()
    else:
        print "Updating airports database..."

    result = openFlights.update_airports()

    return HttpResponse(result, content_type="application/json")
