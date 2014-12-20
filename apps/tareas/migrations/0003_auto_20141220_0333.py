# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_tarea_asignadoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(to='proyectos.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
