from django.core import serializers
from django.http import HttpResponse
from backend.apps.hotels.models import *


def continents(request):
    response_data = serializers.serialize("json", Continent.objects.all())
    return HttpResponse(response_data, content_type="application/json")

def countries(request):
    response_data = serializers.serialize("json", Country.objects.all())
    return HttpResponse(response_data, content_type="application/json")

def destinations(request):
    response_data = serializers.serialize("json", Destination.objects.all())
    return HttpResponse(response_data, content_type="application/json")

def cities(request):
    response_data = serializers.serialize("json", City.objects.all())
    return HttpResponse(response_data, content_type="application/json")

def hotels(request):
    response_data = serializers.serialize("json", Hotel.objects.all())
    return HttpResponse(response_data, content_type="application/json")

def airports(request):
    response_data = serializers.serialize("json", Airport.objects.all())
    return HttpResponse(response_data, content_type="application/json")
