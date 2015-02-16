__author__ = 'Manu'

from django.conf.urls import patterns, url

from backend.apps.providers import views

urlpatterns = patterns('',
    url(r'^', views.providers),
)

