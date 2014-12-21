# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_auto_20141216_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaRegistro',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
