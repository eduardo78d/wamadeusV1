from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import vistaPrincipal, registro, cerrarSesion

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wamadeusV1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^$', 'django.contrib.auth.views.login',{'template_name':'home.html'}, name='login' ),#Sistema de Autentificacion

    #url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name='logout'),

    url(r'^$', vistaPrincipal ,name='home'),  

    url(r'^cerrarSesion/$', cerrarSesion ,name='cerrarSesion'),  

    url(r'^registro/$', registro, name='registro'),

    url(r'^usuario/', include('apps.usuarios.urls')),

    url(r'^proyecto/', include('apps.proyectos.urls')),

)


