# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0007_auto_20150419_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
