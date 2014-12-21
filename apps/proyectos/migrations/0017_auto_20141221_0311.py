# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0016_auto_20141221_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
