# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20161124_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChoreDebil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('last_chore', models.DateField(null=True)),
                ('weight', models.IntegerField()),
                ('chore', models.ForeignKey(to='work.Chore')),
                ('debil', models.ForeignKey(to='orders.Debil', verbose_name='déBIL')),
            ],
        ),
        migrations.AddField(
            model_name='chore',
            name='chorables',
            field=models.ManyToManyField(to='orders.Debil', through='work.ChoreDebil'),
        ),
    ]
