from django.contrib import admin

from solo.admin import SingletonModelAdmin
from backend.apps.giata.models import *

admin.site.register(Giata, SingletonModelAdmin)