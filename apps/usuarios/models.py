from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	#eduardo78d xxpesar1020
	usuario = models.OneToOneField(User)
	
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)

	telefono = models.IntegerField()
	imagen = models.ImageField(upload_to='profile_image')
	descripcion = models.TextField(max_length=300)
	status = models.BooleanField(default=False)


	def __unicode__(self):
		return self.usuario.username