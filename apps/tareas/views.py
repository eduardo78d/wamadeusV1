from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.proyectos.models import Proyecto, Estado

from .forms import FormularioTarea
from .models import Tarea

#Decoradores Temporales
def getTarea(id_tarea):
	return Tarea.objects.get(id=id_tarea)

def getUsuario(id_usuario):
	return Usuario.objects.get(usuario_id=id_usuario)

def getProyecto(id_project):
	return Proyecto.objects.get(id=id_project)

def isAdminProject(id_usuario, id_project):
	if getUsuario(id_usuario) == getProyecto(id_project).creador:
		return True
	else:
		return False


@login_required(login_url='/')
def crear(request, name_project , id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	if request.method == 'POST':
		form = FormularioTarea(request.POST)
		if form.is_valid():
			newHomework = form.save(commit=False)
			newHomework.nombre = form.cleaned_data['nombre'].replace(" ", "_")
			newHomework.proyecto = currentProject
			newHomework.save()
			return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))
		else:
			return redirect('registroTarea', name_project=str(name_project), id_project=str(id_project))
	else:
		return render(request, 'tarea/registro.html', {'usuario': request.user.username,
														'proyecto': currentProject,
														'administrador': True, 'formulario':FormularioTarea})

@login_required(login_url='/')
def asignar(request, name_project, id_project, id_homework):
	tarea = getTarea(id_homework)
	tarea.asignadoA = getUsuario(request.user.id)
	tarea.save()
	return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))

@login_required(login_url='/')
def misActividades(request, name_project, id_project):
	currentProject = getProyecto(id_project)
	usuario = getUsuario(request.user.id)
	estadoFinalizado = Estado.objects.get(nombre='Finalizado')
	administrador = isAdminProject( request.user.id, id_project)
	
	LAF = Tarea.objects.all().filter(asignadoA=usuario, estado=estadoFinalizado, proyecto=currentProject)
	LAA = Tarea.objects.all().filter(proyecto=currentProject).exclude(estado=estadoFinalizado)

	return render(request, 'tarea/misActividades.html', {'usuario': request.user.username,
														'proyecto': currentProject, 
														'administrador':administrador ,
														'listaActividadesActivas': LAA,
														'listaActividadesFinalizadas': LAF})

@login_required(login_url='/')
def editar(request, name_project, id_project, id_homework): #Validar Admin
	currentProject = getProyecto(id_project)
	tarea = getTarea(id_homework)

	if request.method == 'POST':
		form = FormularioTarea(request.POST, instance=tarea)
		if form.is_valid():
			uTarea = form.save(commit=False)
			uTarea.proyecto= currentProject
			uTarea.save()
			return redirect('editarTarea', name_project= name_project, id_project=id_project, id_homework=id_homework)
	else:
		print "Vamos a editar el proyecto"
		form = FormularioTarea(instance=tarea)
		administrador = isAdminProject( request.user.id, id_project)
		return render(request, 'tarea/editar.html', {'usuario': request.user.username,
													'administrador': administrador,
													'proyecto':currentProject,
													'formulario':form, 'tarea': tarea})
	
@login_required(login_url='/')
def eliminar(request, name_project, id_project,id_homework):
	currentProject = getProyecto(id_project)
	tarea = getTarea(id_homework)
	if request.method == 'POST':
		tarea.delete()
		return redirect('proyecto', name_project=name_project, id_project=id_project)
	else:
		return render(request, 'tarea/eliminar.html', {'usuario': request.user.username,
														'administrador':True, 'proyecto':currentProject,
														'tarea': tarea})
@login_required(login_url='/')
def tarea(request, id_homework):
	tarea = getTarea(id_homework)
	return render(request, 'tarea/tarea.html' , {'usuario': request.user.username,
												'tarea': tarea})