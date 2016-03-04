# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_pizza_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='calories',
            field=models.IntegerField(null=True),
        ),
    ]
