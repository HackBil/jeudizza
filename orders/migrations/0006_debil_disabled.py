# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='debil',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
