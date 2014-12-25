from django.conf.urls import patterns, url


from .views import colaboradores

urlpatterns = patterns('',
    
    url(r'^(?P<name_project>\w+)/(?P<id_project>[0-9]+)/$',colaboradores,name='colaboradores'),

)
