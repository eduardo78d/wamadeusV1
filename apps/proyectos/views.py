from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import FormularioProyecto

from apps.usuarios.models import Usuario
from apps.tareas.models import Tarea 

from .models import Proyecto, Estado


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
def nuevo(request):
	if request.method == 'POST':
		usuario = getUsuario(request.user.id)
		form = FormularioProyecto(request.POST)
		if form.is_valid():
			newProject = form.save(commit=False)
			newProject.nombre = form.cleaned_data['nombre'].replace(" ", "_")
			newProject.creador = usuario
			newProject.save()
			return redirect('proyecto', name_project=str(newProject.nombre), id_project=str(newProject.id))
		else:
			return redirect('nuevoProyecto')
	else:
		return render(request, 'proyecto/registro.html',{'usuario': request.user.username,
														'formulario': FormularioProyecto})


@login_required(login_url='/')
def proyecto(request, name_project, id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	estadoFinalizado = Estado.objects.get(nombre='Finalizado')

	LTS = Tarea.objects.all().filter(proyecto=currentProject, asignadoA=None)
	LTA = Tarea.objects.all().filter(proyecto=currentProject).exclude(estado=estadoFinalizado).exclude(asignadoA=None)
	LTF = Tarea.objects.all().filter(proyecto=currentProject, estado=estadoFinalizado).exclude(asignadoA=None)

	administrador = isAdminProject(request.user.id, id_project)
	return render(request, 'proyecto/proyecto.html', {'usuario': request.user.username,
														'proyecto':currentProject,
														'administrador': administrador,
														'listaTareasSinAsignar':LTS,
														'listaTareasActivas': LTA,
														'listaTareasFinalizadas': LTF})

@login_required(login_url='/')
def editar(request, name_project, id_project):
	usuario = Usuario.objects.get(id=request.user.id)  #Corregir esta consulta
	currentProject = Proyecto.objects.get(id=id_project)

	if usuario == currentProject.creador:
		if request.method == 'POST':
			form = FormularioProyecto(request.POST, instance=currentProject)
			if form.is_valid():
				newProject = form.save(commit=False)
				newProject.creador = usuario
				newProject.save()
				return redirect('editarProyecto', name_project=str(name_project), id_project=str(id_project))
		else:
			formulario = FormularioProyecto(instance=currentProject)
			return render(request, 'proyecto/editar.html' , {'usuario': request.user.username,
															'proyecto': currentProject,
															'administrador': True, 'formulario': formulario})
	else:
		return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))

@login_required(login_url='/')
def eliminar(request, name_project, id_project):
	proyecto = getProyecto(id_project)
	if request.method == 'POST':
		proyecto.delete()
		return redirect('perfil')
	else:
		return render(request, 'proyecto/eliminar.html', {'usuario': request.user.username,
														'proyecto': proyecto})