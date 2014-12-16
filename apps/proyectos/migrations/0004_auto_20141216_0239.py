# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_proyecto_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='estado',
        ),
        migrations.AddField(
            model_name='estado',
            name='proyecto',
            field=models.ForeignKey(default=0, to='proyectos.Proyecto'),
            preserve_default=False,
        ),
    ]
