from django.shortcuts import render, redirect
from .forms import FormularioUsuario
from .models import Usuario


# Create your views here.
def perfil(request):
	username = None
	if request.user.is_authenticated():
		username= request.user.username
		return render(request, 'usuario/perfil.html', {'usuario': username})

def editarPerfil(request):
	#Valores apellidos, correo, descripcion, id, imagen, nombre, status, telefono, usuario, usuario_id
	username = None
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
		
		
		
		