from django.conf.urls import patterns, url


from .views import crear,asignar,misActividades, editar , eliminar, tarea

urlpatterns = patterns('',
 
    url(r'nuevo/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',crear,name='registroTarea'),   

	url(r'asignar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/(?P<id_homework>[0-9]+)/$',asignar,name='asignarTarea'),   

	url(r'mis_actividades/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',misActividades,name='misActividades'),   

	url(r'editar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/(?P<id_homework>[0-9]+)/$',editar,name='editarTarea'),   

	url(r'eliminar/(?P<name_project>\w+)/(?P<id_project>[0-9]+)/(?P<id_homework>[0-9]+)/$',eliminar,name='eliminarTarea'),   

	url(r'^tarea/(?P<id_homework>[0-9]+)/$',tarea, name='tarea'),
)