# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(upload_to=b'imagenes/profile_image'),
            preserve_default=True,
        ),
    ]
