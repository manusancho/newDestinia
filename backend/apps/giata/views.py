import os
from django.http import HttpResponse

from backend.apps.giata.models import *


def giata_update_all(request):

    giata = Giata.get_solo()

    # Update countries
    result = giata.update_countries()
    if result is False:
        # TODO: log error
        return HttpResponse(result, content_type="application/json")

    # Update destinations
    result += giata.update_destinations()
    if result is False:
        # TODO: log error
        return HttpResponse(result, content_type="application/json")

    # Update cities
    result += giata.update_cities()
    if result is False:
        # TODO: log error
        return HttpResponse(result, content_type="application/json")

    # Update hotels
    result += giata.update_hotels()
    if result is False:
        # TODO: log error
        return HttpResponse(result, content_type="application/json")

    return HttpResponse(result, content_type="application/json")


def giata_update_countries(request):

    giata = Giata.get_solo()

    # Update countries
    result = giata.update_countries()

    return HttpResponse(result, content_type="application/json")


def giata_update_destinations(request):

    giata = Giata.get_solo()

    # Update destinations
    result = giata.update_destinations()

    return HttpResponse(result, content_type="application/json")


def giata_update_cities(request):

    giata = Giata.get_solo()

    # Update cities
    result = giata.update_cities()

    return HttpResponse(result, content_type="application/json")


def giata_update_hotels(request):

    # Update hotels
    result = giata.update_hotels()

    return HttpResponse(result, content_type="application/json")

