from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import FormularioProyecto

from apps.usuarios.models import Usuario
from .models import Proyecto

def nuevo(request):
	if request.method == 'POST':
		usuario = Usuario.objects.get(usuario=request.user)
		form = FormularioProyecto(request.POST)
		if form.is_valid():
			newProject = form.save(commit=False)
			newProject.creador = usuario
			newProject.save()

			return redirect('proyecto', name_project=str(newProject.nombre.replace(" ", "_")), id_project=str(newProject.id))
		else:
			return redirect('nuevoProyecto')
	else:
		return render(request, 'proyecto/registro.html',{'formulario': FormularioProyecto})

def proyecto(request, name_project, id_project):
	currentProject = Proyecto.objects.get(id=id_project)
	usuario = Usuario.objects.get(id=request.user.id)
	
	if usuario == currentProject.creador:
		admin = True
	else:
		admin = False
	return render(request, 'proyecto/proyecto.html', {'proyecto':currentProject,
														'administrador': admin})

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
			return render(request, 'proyecto/editar.html' , {'proyecto': currentProject
															,'administrador': True, 'formulario': formulario})
	else:
		return redirect('proyecto', name_project=str(name_project), id_project=str(id_project))