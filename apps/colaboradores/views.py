from django.shortcuts import render
from apps.proyectos.models import Proyecto

# Create your views here.
def colaboradores(request, name_project , id_project):
	proyecto = Proyecto.objects.get(id=id_project)
	return render(request, 'colaborador/colaboradores.html',{'usuario': request.user.username,
															'proyecto': proyecto,
															'administrador': True})