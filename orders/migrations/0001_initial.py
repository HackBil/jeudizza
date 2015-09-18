# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('overprice', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Debil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('company', models.ForeignKey(to='orders.Company', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('open', models.BooleanField(default=True)),
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
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crust', models.ForeignKey(to='orders.Crust')),
                ('debil', models.ForeignKey(to='orders.Debil')),
                ('order', models.ForeignKey(to='orders.Order')),
                ('pizza', models.ForeignKey(to='orders.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizza_set',
            field=models.ManyToManyField(to='orders.Pizza', through='orders.PizzaOrder'),
        ),
    ]
