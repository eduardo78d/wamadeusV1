from django.db import models

from apps.proyectos.models import Estado, Proyecto
from apps.usuarios.models import Usuario
# Create your models here.

class Tarea(models.Model):
	nombre= models.CharField(max_length=50)

	asignadoA = models.ForeignKey(Usuario, null=True, blank=True)

	proyecto = models.ForeignKey(Proyecto)
	descripcion= models.TextField(max_length=200)
	fechaInicio= models.DateField()
	fechaEntrega= models.DateField()
	estado= models.ForeignKey(Estado)

	def __str__(self):
		return self.nombre