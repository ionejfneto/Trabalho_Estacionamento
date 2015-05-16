# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='hora',
            new_name='horaEntrada',
        ),
        migrations.AddField(
            model_name='vaga',
            name='horaSaida',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
