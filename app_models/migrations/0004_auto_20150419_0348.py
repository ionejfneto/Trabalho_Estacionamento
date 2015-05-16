# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0003_auto_20150419_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='descricao',
            field=models.CharField(default=b'vazia', max_length=100, blank=True),
        ),
    ]
