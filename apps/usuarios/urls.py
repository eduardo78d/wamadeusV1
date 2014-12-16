from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import perfil, editarPerfil

urlpatterns = patterns('',
    
    url(r'perfil/$',perfil,name='perfil'),

    url(r'perfil/editar$',editarPerfil,name='editarPerfil'),
    
    
)
