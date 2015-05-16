# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=150)),
                ('dataCad', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('numero', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('carro', models.ForeignKey(verbose_name=b'Carro', to='app_models.Carro')),
                ('dono', models.ForeignKey(verbose_name=b'Cliente', to='app_models.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='carro',
            name='dono',
            field=models.ForeignKey(verbose_name=b'Cliente', to='app_models.Cliente'),
            preserve_default=True,
        ),
    ]
