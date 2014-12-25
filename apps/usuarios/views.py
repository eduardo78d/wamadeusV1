from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import FormularioUsuario
from .models import Usuario
from apps.proyectos.models import Proyecto


@login_required(login_url='/')
def perfil(request):
	listadoProyectos = Proyecto.objects.filter(creador= request.user)
	return render(request, 'usuario/perfil.html', {'usuario': request.user.username,
														'listadoProyectos':listadoProyectos})
@login_required(login_url='/')
def editarPerfil(request):
	#Valores apellidos, correo, descripcion, id, imagen, nombre, status, telefono, usuario, usuario_id
	
	usuario = Usuario.objects.get(usuario_id=request.user.id)
	if request.method == 'POST':
		myform = FormularioUsuario(request.POST, instance=usuario)
		
		if myform.is_valid():
			myform.save()
			return redirect ('editarPerfil')
		else:
			return redirect ('editarPerfil')
	else:
		form = FormularioUsuario(instance=usuario)
		return render(request, 'usuario/editar.html', {'usuario': request.user.username, 'formulario':form})
	
		
		
		