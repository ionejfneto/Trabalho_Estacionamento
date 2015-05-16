# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0009_auto_20150420_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Pagamento',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
