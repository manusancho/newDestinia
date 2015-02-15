from django.conf.urls import patterns, static, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'backend.views.home', name='home'),

    url(r'^continents', 'backend.apps.hotels.views.continents', name='continents'),
    url(r'^countries', 'backend.apps.hotels.views.countries', name='countries'),
    url(r'^destinations', 'backend.apps.hotels.views.destinations', name='destinations'),
    url(r'^cities', 'backend.apps.hotels.views.cities', name='cities'),
    url(r'^hotels', 'backend.apps.hotels.views.hotels', name='hotels'),

    url(r'^providers', 'backend.apps.providers.views.providers', name='providers'),

    url(r'^giata/update', 'backend.apps.giata.views.giata_update_all', name='giata_update_all'),
    url(r'^giata/update/countries', 'backend.apps.giata.views.giata_update_countries', name='giata_update_countries'),
    url(r'^giata/update/destinations', 'backend.apps.giata.views.giata_update_destinations', name='giata_update_destinations'),
    url(r'^giata/update/cities', 'backend.apps.giata.views.giata_update_cities', name='giata_update_cities'),
    url(r'^giata/update/hotels', 'backend.apps.giata.views.giata_update_hotels', name='giata_update_hotels'),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)