from django.shortcuts import render
from django.http import HttpResponse
import os

from backend.apps.giata.models import *


def giata_update_all(request):

    giata = Giata.get_solo()

    # Update countries
    return HttpResponse("all", content_type="application/json")
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

    return HttpResponse("cuntries", content_type="application/json")
    giata = Giata.get_solo()

    # Update countries
    result = giata.update_countries()

    return HttpResponse(result, content_type="application/json")


def giata_update_destinations(request):

    return HttpResponse("dest", content_type="application/json")
    giata = Giata.get_solo()

    # Update destinations
    result = giata.update_destinations()

    return HttpResponse(result, content_type="application/json")


def giata_update_cities(request):

    return HttpResponse("cit", content_type="application/json")
    giata = Giata.get_solo()

    # Update cities
    result = giata.update_cities()

    return HttpResponse(result, content_type="application/json")


def giata_update_hotels(request):

    return HttpResponse("hotels", content_type="application/json")
    giata = Giata.get_solo()

    # Update hotels
    result = giata.update_hotels()

    return HttpResponse(result, content_type="application/json")

