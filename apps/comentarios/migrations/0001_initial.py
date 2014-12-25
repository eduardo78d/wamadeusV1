# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0005_auto_20141220_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'30')),
                ('descripcion', models.TextField(max_length=b'100')),
                ('color', models.CharField(max_length=b'10')),
                ('tarea', models.ForeignKey(to='tareas.Tarea')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
