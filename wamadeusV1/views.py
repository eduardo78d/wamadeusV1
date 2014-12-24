from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login , logout


from .forms import UserForm
from apps.usuarios.models import Usuario

def vistaPrincipal(request):
	if request.user.is_authenticated():
		return render(request, 'vistaPrincipal.html', {})
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return render(request, 'vistaPrincipal.html', {})
				else:
					return redirect('home')	
		else:
			return render(request, 'home.html', {})

def cerrarSesion(request):
	logout(request)
	return redirect('home')

def registro(request):
	if request.user.is_authenticated()==False:
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				user = form.save()
				nuevoUsuario = Usuario()
				nuevoUsuario.usuario = user
				nuevoUsuario.correo = form.cleaned_data['correo']
				nuevoUsuario.telefono = 0
				nuevoUsuario.save()
				return redirect('home')		
			else:
				return redirect('registro')
		else:
			return render(request, 'usuario/registro.html' ,{'formulario':UserForm})
	else:
		return redirect('home')