# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
