# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_auto_20141216_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='proyecto',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='id',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.ForeignKey(default=0, to='proyectos.Estado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(primary_key=True, serialize=False, to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
