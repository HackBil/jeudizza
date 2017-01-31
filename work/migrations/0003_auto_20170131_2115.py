# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20161124_1528'),
        ('work', '0002_auto_20170131_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='last_debil',
            field=models.ForeignKey(null=True, verbose_name='déBIL', related_name='last_chores_set', to='orders.Debil', blank=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='chorables',
            field=models.ManyToManyField(related_name='chorables_set', to='orders.Debil', through='work.ChoreDebil'),
        ),
    ]
