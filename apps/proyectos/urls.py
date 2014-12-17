from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import nuevo, proyecto

urlpatterns = patterns('',
    
    url(r'nuevo/$',nuevo,name='nuevoProyecto'),

    url(r'actual/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',proyecto,name='proyecto'),

)
