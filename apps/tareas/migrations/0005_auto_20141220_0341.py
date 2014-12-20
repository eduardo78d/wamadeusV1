# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_auto_20141220_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='asignadoA',
            field=models.ForeignKey(blank=True, to='usuarios.Usuario', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(default=0, to='proyectos.Proyecto'),
            preserve_default=False,
        ),
    ]
