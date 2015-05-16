# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0011_remove_cliente_pagamento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='vaga',
            options={'ordering': ['horaSaida']},
        ),
        migrations.RenameField(
            model_name='vaga',
            old_name='horaEntrada',
            new_name='entrada',
        ),
        migrations.AlterField(
            model_name='vaga',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
