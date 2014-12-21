from django import forms
from django.forms import ModelForm

import datetime

from .models import Tarea

class FormularioTarea(ModelForm):
	class Meta: 
		model = Tarea
		
		widgets = {
			'fechaInicio' : forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'Ejemplo 1/1/2015'}),
			'fechaEntrega': forms.DateInput(format='%d/%m/%Y' , attrs={'placeholder': 'Ejemplo 31/12/2015'})
		}

		exclude = ['proyecto', 'asignadoA']