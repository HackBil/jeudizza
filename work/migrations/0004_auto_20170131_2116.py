# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20170131_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='last_execution',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='last_debil',
            field=models.ForeignKey(null=True, to='orders.Debil', related_name='last_chores_set', blank=True),
        ),
    ]
