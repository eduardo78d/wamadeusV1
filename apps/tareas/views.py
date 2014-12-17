from django.shortcuts import render
from apps.usuarios.models import Usuario
from apps.proyectos.models import Proyecto

from .forms import FormularioTarea

# Create your views here.
def registro(request, name_project , id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	usuario = Usuario.objects.get(id=request.user.id)
	return render(request, 'tarea/registro.html', {'proyecto': currentProject
													,'administrador': True, 'formulario':FormularioTarea})
	
