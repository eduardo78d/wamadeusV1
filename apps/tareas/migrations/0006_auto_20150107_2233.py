# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0005_auto_20141220_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaInicio',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
