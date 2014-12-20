# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_correo'),
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='asignadoA',
            field=models.ForeignKey(default=0, to='usuarios.Usuario'),
            preserve_default=False,
        ),
    ]
