from django.db import models
from apps.tareas.models import Tarea

# Create your models here.
class Comentario(models.Model):
	tarea = models.ForeignKey(Tarea)
	nombre = models.CharField(max_length='30')
	descripcion = models.TextField(max_length='100')
	color = models.CharField(max_length='10')

	def __unicode__(self):
		return self.nombre