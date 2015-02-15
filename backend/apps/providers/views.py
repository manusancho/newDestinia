from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from backend.apps.providers.models import *

def providers(request):
    response_data = serializers.serialize("json",Provider.objects.all())
    return HttpResponse(response_data, content_type="application/json")