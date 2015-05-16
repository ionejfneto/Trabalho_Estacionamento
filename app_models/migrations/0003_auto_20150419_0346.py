# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0002_auto_20150419_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='horaSaida',
            field=models.TimeField(blank=True),
        ),
    ]
