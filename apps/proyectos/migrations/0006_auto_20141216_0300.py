# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20141216_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
