from django.contrib import admin

# Register your models here.
from backend.apps.hotels.models import *

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Hotel)