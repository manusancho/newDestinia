__author__ = 'Manu'

from django.conf.urls import patterns, url

from backend.apps.giata import views

urlpatterns = patterns('',
    url(r'^giata/update', views.giata_update_all),
    url(r'^countries/update', views.giata_update_countries),
    url(r'^destinations/update', views.giata_update_destinations),
    url(r'^cities/update', views.giata_update_cities),
    url(r'^hotels/update', views.giata_update_hotels),
)