from django.contrib import admin

from solo.admin import SingletonModelAdmin
from backend.apps.siteConfiguration.models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)