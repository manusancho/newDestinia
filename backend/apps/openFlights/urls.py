__author__ = 'Manu'

from django.conf.urls import patterns, url

from backend.apps.openFlights import views

urlpatterns = patterns('',
    url(r'^airports/update/?$', views.update_airports),
)