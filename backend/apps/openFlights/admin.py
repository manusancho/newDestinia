from django.contrib import admin

from solo.admin import SingletonModelAdmin
from backend.apps.openFlights.models import *

admin.site.register(OpenFlights, SingletonModelAdmin)
