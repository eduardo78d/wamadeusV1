from django.db import models

from apps.proyectos.models import Estado, Proyecto
# Create your models here.

class Tarea(models.Model):
	nombre= models.CharField(max_length=50)
	proyecto = models.ForeignKey(Proyecto)
	descripcion= models.TextField(max_length=200)
	fechaInicio= models.DateField()
	fechaEntrega= models.DateField()
	estado= models.ForeignKey(Estado)