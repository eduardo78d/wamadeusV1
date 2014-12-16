from django.db import models
from apps.usuarios.models import Usuario
from datetime import datetime

class Estado(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField(max_length=100)
	color = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Proyecto(models.Model):
	creador = models.ForeignKey(Usuario)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=100)
	estado = models.OneToOneField(Estado)
	fechaRegistro = models.DateTimeField(default=datetime.now, blank=True)
	

	def __unicode__(self):
		return self.nombre


