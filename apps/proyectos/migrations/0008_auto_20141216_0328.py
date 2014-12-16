# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_auto_20141216_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaRegistro',
            field=models.DateField(default=b'16/12/2014', blank=True),
            preserve_default=True,
        ),
    ]
