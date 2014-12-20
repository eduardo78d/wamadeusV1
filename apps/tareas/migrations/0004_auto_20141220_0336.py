# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_auto_20141220_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='proyectos.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
