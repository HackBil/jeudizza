# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Bilien(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)

    def __unicode__(self):
        return u"%s (%g€)" % (self.name, self.price)


class Order(models.Model):
    pizza_set = models.ManyToManyField(Pizza, through='PizzaBilienOrder')
    date = models.DateField()

    def get_total_price(self):
        total = sum([pizza.price for pizza in self.pizza_set.all()])
        return total


class PizzaBilienOrder(models.Model):
    pizza = models.ForeignKey(Pizza)
    bilien = models.ForeignKey(Bilien)
    order = models.ForeignKey(Order)
