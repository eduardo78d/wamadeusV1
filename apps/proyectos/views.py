from django.shortcuts import render, redirect
from .forms import FormularioProyecto
from apps.usuarios.models import Usuario

# Create your views here.
def nuevo(request):
	if request.method == 'POST':
		usuario = Usuario.objects.get(usuario=request.user)
		form = FormularioProyecto(request.POST)
		if form.is_valid():
			newProject = form.save(commit=False) # commit=False tells Django that "Don't send this to database yet.
			newProject.creador = usuario
			newProject.save()
			return redirect('nuevoProyecto')
		else:
			return redirect('home')
	else:
		return render(request, 'proyecto/registro.html',{'formulario': FormularioProyecto})
