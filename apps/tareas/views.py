from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.proyectos.models import Proyecto

from .forms import FormularioTarea
from .models import Tarea


# Create your views here.
def registro(request, name_project , id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	usuario = Usuario.objects.get(id=request.user.id)
	if request.method == 'POST':
		form = FormularioTarea(request.POST)
		if form.is_valid():
			newHomework = form.save(commit=False)
			newHomework.proyecto = currentProject
			newHomework.save()
			return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))
		else:
			return redirect('registroTarea', name_project=str(name_project), id_project=str(id_project))
	else:
		return render(request, 'tarea/registro.html', {'proyecto': currentProject
													,'administrador': True, 'formulario':FormularioTarea})
	
def asignar(request, name_project, id_project, id_homework):
	homework = Tarea.objects.get(id=id_homework)
	homework.asignadoA = Usuario.objects.get(id=request.user.id)
	homework.save()
	return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))

def misActividades(request, name_project, id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	usuario = Usuario.objects.get(id=request.user.id)
	if usuario == currentProject.creador:
		admin = True
	else:
		admin = False
	return render(request, 'tarea/misActividades.html', {'proyecto': currentProject, 'administrador':admin })