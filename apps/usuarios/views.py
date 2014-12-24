from django.shortcuts import render, redirect
from .forms import FormularioUsuario
from .models import Usuario
from apps.proyectos.models import Proyecto

# Create your views here.
def perfil(request):
	if request.user.is_authenticated():
		listadoProyectos = Proyecto.objects.filter(creador= request.user)
		return render(request, 'usuario/perfil.html', {'usuario': request.user.username,
														'listadoProyectos':listadoProyectos})

def editarPerfil(request):
	#Valores apellidos, correo, descripcion, id, imagen, nombre, status, telefono, usuario, usuario_id
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(usuario=request.user)
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
		
		
		
		