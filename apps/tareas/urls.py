from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import registro

urlpatterns = patterns('',
 
    url(r'nuevo/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',registro,name='registroTarea'),   
    
)
