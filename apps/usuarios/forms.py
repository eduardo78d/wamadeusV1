#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Usuario


class FormularioUsuario(ModelForm):
	#https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/
	#passwordCon = forms.CharField(label='password de confirmación', widget=forms.PasswordInput, initial='')

	class Meta:
		model = Usuario
		fields = ['nombre', 'apellidos', 'correo', 'telefono' ,'descripcion', 'imagen'] 