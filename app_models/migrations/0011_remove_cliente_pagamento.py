# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0010_cliente_pagamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Pagamento',
        ),
    ]
