# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150417_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='crust',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='crust',
            field=models.ForeignKey(verbose_name='croute', to='orders.Crust'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='debil',
            field=models.ForeignKey(verbose_name='d\xe9BIL', to='orders.Debil'),
        ),
    ]
