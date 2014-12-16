from django import forms
from django.forms import ModelForm
from .models import Proyecto


class FormularioProyecto(ModelForm):
	class Meta:
		model = Proyecto
		fields = ['nombre', 'descripcion', 'estado']
		