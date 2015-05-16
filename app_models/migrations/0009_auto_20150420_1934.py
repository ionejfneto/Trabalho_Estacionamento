# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0008_auto_20150420_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dataCad',
            field=models.DateField(auto_now_add=True),
        ),
    ]
