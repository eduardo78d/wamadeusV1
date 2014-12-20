from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import registro,asignar,misActividades

urlpatterns = patterns('',
 
    url(r'nuevo/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',registro,name='registroTarea'),   

	url(r'asignar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/(?P<id_homework>[0-9]+)/$',asignar,name='asignarTarea'),   

	url(r'misActividades/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',misActividades,name='misActividades'),   

)