# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=100)),
                ('color', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('fechaRegistro', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('creador', models.ForeignKey(to='usuarios.Usuario')),
                ('estado', models.OneToOneField(to='proyectos.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
