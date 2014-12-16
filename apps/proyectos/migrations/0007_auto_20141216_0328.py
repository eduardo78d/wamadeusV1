# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20141216_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaRegistro',
            field=models.DateTimeField(default=b'16/12/2014', blank=True),
            preserve_default=True,
        ),
    ]
