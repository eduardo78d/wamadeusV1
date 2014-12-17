from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import FormularioProyecto

from apps.usuarios.models import Usuario
from .models import Proyecto

# Create your views here.
def nuevo(request):
	if request.method == 'POST':
		usuario = Usuario.objects.get(usuario=request.user)
		form = FormularioProyecto(request.POST)
		if form.is_valid():
			newProject = form.save(commit=False) # commit=False tells Django that "Don't send this to database yet.
			newProject.creador = usuario
			newProject.save()
			#Debemos de arreglar esto y utilizar un redirect con parametros
			return HttpResponseRedirect('/proyecto/actual/'+ str(newProject.nombre) +'/'+str(newProject.id)+'/') 
		else:
			return redirect('nuevoProyecto')
	else:
		return render(request, 'proyecto/registro.html',{'formulario': FormularioProyecto})

def proyecto(request, name_project, id_project):
	currentProject = Proyecto.objects.get(id=id_project)  #Es posible que esto colapse en algun momento
	usuario = Usuario.objects.get(id=request.user.id)  #Corregir esta consulta
	
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
			form = FormularioProyecto(request.POST)
			if form.is_valid():
				newProject = form.save(commit=False) # commit=False tells Django that "Don't send this to database yet.
				newProject.creador = usuario
				newProject.save()
				return HttpResponseRedirect('/proyecto/editar/'+ str(name_project) +'/'+str(id_project)+'/') 
		else:
			formulario = FormularioProyecto(instance=currentProject)
			return render(request, 'proyecto/editar.html' , {'administrador': True, 'formulario': formulario})
	else:
		return HttpResponseRedirect('/proyecto/actual/'+ str(name_project) +'/'+str(id_project)+'/') 

	