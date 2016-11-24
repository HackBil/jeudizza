# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrepeOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('price', models.FloatField(null=True)),
                ('open', models.BooleanField(default=True)),
                ('debil', models.ManyToManyField(verbose_name='déBIL', to='orders.Debil')),
            ],
        ),
    ]
