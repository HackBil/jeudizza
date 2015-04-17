from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)


class Bilien(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, null=True)


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)


class Order(models.Model):
    pizza_set = models.ManyToManyField(Pizza, through='PizzaBilienOrder')
    date = models.DateField()


class PizzaBilienOrder(models.Model):
    pizza = models.ForeignKey(Pizza)
    bilien = models.ForeignKey(Bilien)
    order = models.ForeignKey(Order)
