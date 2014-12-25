from django.conf.urls import patterns, include, url


from .views import nuevo, proyecto, editar, eliminar

urlpatterns = patterns('',
    
    url(r'nuevo/$',nuevo,name='nuevoProyecto'),

    url(r'actual/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',proyecto,name='proyecto'),

    url(r'editar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',editar,name='editarProyecto'),

    url(r'eliminar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',eliminar,name='eliminarProyecto'),

    url(r'tarea/', include('apps.tareas.urls')),

    url(r'colaboradores/', include('apps.colaboradores.urls')),
)
