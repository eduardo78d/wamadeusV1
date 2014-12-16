# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_remove_proyecto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.OneToOneField(default=0, to='proyectos.Estado'),
            preserve_default=False,
        ),
    ]
