# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def get_price(pizzaOrder):
    return pizzaOrder.pizza.price + pizzaOrder.crust.overprice


def create_previous_depts(apps, schema_editor):
    Debil = apps.get_model("orders", "Debil")
    Dept = apps.get_model("orders", "Dept")
    for debil in Debil.objects.all():
        take = sum([get_price(pizza) for pizza in debil.pizzaorder_set.all()])
        Dept(debil=debil, amount=take).save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_pizza_calories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(null=True, auto_now_add=True)),
                ('debil', models.ForeignKey(to='orders.Debil', verbose_name='déBIL')),
            ],
        ),
        migrations.RunPython(create_previous_depts),
    ]
