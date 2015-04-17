# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256)),
                ('price', models.FloatField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaBilienOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bilien', models.ForeignKey(to='orders.Bilien')),
                ('order', models.ForeignKey(to='orders.Order')),
                ('pizza', models.ForeignKey(to='orders.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizza_set',
            field=models.ManyToManyField(to='orders.Pizza', through='orders.PizzaBilienOrder'),
        ),
        migrations.AddField(
            model_name='bilien',
            name='company',
            field=models.ForeignKey(to='orders.Company', null=True),
        ),
    ]
