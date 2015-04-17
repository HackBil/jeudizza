# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Debil(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Crust(models.Model):
    name = models.CharField(max_length=64, unique=True)
    overprice = models.FloatField(default=0)

    def __unicode__(self):
        return u"%s (+%g€)" % (self.name, self.overprice)


class Pizza(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u"%s (%g€)" % (self.name, self.price)


class Order(models.Model):
    pizza_set = models.ManyToManyField(Pizza, through='PizzaOrder')
    date = models.DateField()
    open = models.BooleanField(default=True)

    def get_pizza_order(self):
        return PizzaOrder.objects.filter(order=self)

    def get_total_price(self):
        pizza_orders = self.get_pizza_order()

        total = sum([pizza.get_price() for pizza in pizza_orders])
        return total


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza)
    debil = models.ForeignKey(Debil, verbose_name=u'déBIL')
    order = models.ForeignKey(Order)
    crust = models.ForeignKey(Crust, verbose_name=u'croute')

    def get_price(self):
        return self.pizza.price + self.crust.overprice
