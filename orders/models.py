# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Debil(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Crust(models.Model):
    name = models.CharField(max_length=64)
    overprice = models.FloatField(default=0)

    def __unicode__(self):
        return u"%s (+%g€)" % (self.name, self.overprice)


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)

    def __unicode__(self):
        return u"%s (%g€)" % (self.name, self.price)


class Order(models.Model):
    pizza_set = models.ManyToManyField(Pizza, through='PizzaOrder')
    date = models.DateField()
    open = models.BooleanField(default=True)

    def get_total_price(self):
        total = sum([pizza.get_price for pizza in self.pizza_set.all()])
        return total


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza)
    debil = models.ForeignKey(Debil)
    order = models.ForeignKey(Order)
    crust = models.ForeignKey(Crust)

    def get_price(self):
        return self.pizza.price + self.crust.overprice
