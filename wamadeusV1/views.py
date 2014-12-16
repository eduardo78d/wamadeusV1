from django.shortcuts import render
from django.shortcuts import redirect

from .forms import UserForm
from apps.usuarios.models import Usuario


def home(request):
	username = None
	if request.user.is_authenticated():
		username= request.user.username
		return render(request, 'usuario/vistaPrincipal.html', {'usuario': username})

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
			else:
				return redirect('registro')
		else:
			return render(request, 'usuario/registro.html' ,{'formulario':UserForm})
	else:
		return redirect('home')