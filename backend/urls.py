from django.conf.urls import patterns, static, include, url
from django.contrib import admin
from django.conf import settings

from backend import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),

    url(r'^', include('backend.apps.giata.urls')),
    url(r'^', include('backend.apps.openFlights.urls')),

    url(r'^', include('backend.apps.hotels.urls')),
    url(r'^providers', include('backend.apps.providers.urls')),

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)