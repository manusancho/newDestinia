__author__ = 'Manu'

from django.conf.urls import patterns, url

from backend.apps.hotels import views

urlpatterns = patterns('',
    url(r'^continents', views.continents),
    url(r'^countries', views.countries),
    url(r'^destinations', views.destinations),
    url(r'^cities', views.cities),
    url(r'^hotels', views.hotels),
    url(r'^airports', views.airports),
)


