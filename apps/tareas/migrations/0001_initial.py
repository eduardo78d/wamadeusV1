# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_auto_20141216_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('fechaInicio', models.DateField()),
                ('fechaEntrega', models.DateField()),
                ('estado', models.ForeignKey(to='proyectos.Estado')),
                ('proyecto', models.ForeignKey(to='proyectos.Proyecto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
