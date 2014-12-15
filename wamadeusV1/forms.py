from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	#telefono = forms.IntegerField()
	correo = forms.EmailField(label='Correo Electronico')