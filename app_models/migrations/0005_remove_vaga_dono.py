# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0004_auto_20150419_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='dono',
        ),
    ]
