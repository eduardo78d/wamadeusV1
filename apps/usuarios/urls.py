from django.conf.urls import patterns, url


from .views import perfil, editar

urlpatterns = patterns('',
    
    url(r'perfil/$',perfil,name='perfil'),

    url(r'perfil/editar$',editar,name='editarPerfil'),

)
