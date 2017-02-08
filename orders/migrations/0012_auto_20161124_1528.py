# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_crepeorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crepeorder',
            name='debil',
        ),
        migrations.AddField(
            model_name='crepeorder',
            name='debil_set',
            field=models.ManyToManyField(related_name='crepeOrders', to='orders.Debil', verbose_name='déBIL', blank=True),
        ),
        migrations.AlterField(
            model_name='crepeorder',
            name='price',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
