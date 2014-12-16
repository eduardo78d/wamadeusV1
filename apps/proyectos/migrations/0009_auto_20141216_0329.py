# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0008_auto_20141216_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaRegistro',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
    ]
