from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.proyectos.models import Proyecto, Estado

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

	estadoFinalizado = Estado.objects.get(nombre='Finalizado')

	if usuario == currentProject.creador:
		admin = True
	else:
		admin = False
	LAF = Tarea.objects.all().filter(asignadoA=usuario, estado=estadoFinalizado)
	LAA = Tarea.objects.all().filter().exclude(estado=estadoFinalizado)

	return render(request, 'tarea/misActividades.html', {'proyecto': currentProject, 'administrador':admin ,
														'listaActividadesActivas': LAA,
														'listaActividadesFinalizadas': LAF})

def tarea(request, name_project, id_project, id_homework): #Validar Admin
	currentProject = Proyecto.objects.get(id=id_project)
	tarea = Tarea.objects.get(id=id_homework)

	if request.method == 'POST':
		form = FormularioTarea(request.POST, instance=tarea)
		if form.is_valid():
			uTarea = form.save(commit=False)
			uTarea.proyecto= currentProject
			uTarea.save()
			return redirect('tarea', name_project= name_project, id_project=id_project, id_homework=id_homework)
	else:
		form = FormularioTarea(instance=tarea)
		return render(request, 'tarea/tarea.html', {'administrador':True, 'proyecto':currentProject,
												'formulario':form, 'tarea': tarea})

def eliminarTarea(request, name_project, id_project,id_homework):
	currentProject = Proyecto.objects.get(id=id_project)
	tarea = Tarea.objects.get(id=id_homework)
	if request.method == 'POST':
		tarea.delete()
		return redirect('proyecto', name_project=name_project, id_project=id_project)
	else:
		return render(request, 'tarea/eliminar.html', {'administrador':True, 'proyecto':currentProject,
												'tarea': tarea})

