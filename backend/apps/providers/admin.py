from django.contrib import admin

# Register your models here.
from backend.apps.providers.models import *


admin.site.register(Provider, ProviderAdmin)