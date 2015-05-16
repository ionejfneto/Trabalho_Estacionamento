# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0005_remove_vaga_dono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='descricao',
            field=models.CharField(default=b'vazia', max_length=100),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='horaSaida',
            field=models.TimeField(null=True),
        ),
    ]
