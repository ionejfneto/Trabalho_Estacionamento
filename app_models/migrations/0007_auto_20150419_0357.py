# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0006_auto_20150419_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='horaSaida',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
