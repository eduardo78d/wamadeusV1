#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Usuario


class FormularioUsuario(ModelForm):
	
	class Meta:
		model = Usuario
		fields = ['nombre', 'apellidos', 'correo', 'telefono' ,'descripcion'] 
		#La imagen esta dando problemas
		#Agregra el campo de password para confirmar