# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_previous_payments(apps, schema_editor):
    PizzaOrder = apps.get_model("orders", "PizzaOrder")
    Payment = apps.get_model("orders", "Payment")
    for order in PizzaOrder.objects.all():
        Payment(debil=order.debil, price=order.pizza.price + order.crust.overprice).save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150624_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.FloatField()),
                ('debil', models.ForeignKey(to='orders.Debil', verbose_name='déBIL')),
            ],
        ),
        migrations.RunPython(create_previous_payments),
    ]
