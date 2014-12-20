from django import forms
from django.forms import ModelForm
from .models import Tarea

class FormularioTarea(ModelForm):
	class Meta: 
		model = Tarea
		exclude = ['proyecto', 'asignadoA']