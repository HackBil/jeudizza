# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choredebil',
            name='last_chore',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choredebil',
            name='weight',
            field=models.IntegerField(default=5),
        ),
    ]
