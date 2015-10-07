from django.db import models
from django.db.models import Sum


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Debil(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, null=True)
    disabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_solde(self):
        paid = self.payment_set.aggregate(Sum('price')).get("price__sum") or 0.0
        take = sum([pizza.get_price() for pizza in self.pizzaorder_set.all()])
        return paid - take


class Crust(models.Model):
    name = models.CharField(max_length=64, unique=True)
    overprice = models.FloatField(default=0)

    def __str__(self):
        if self.overprice == 0:
            return self.name
        else:
            return "%s (+%g€)" % (self.name, self.overprice)


class Pizza(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "%s (%g€)" % (self.name, self.price)


class Order(models.Model):
    pizza_set = models.ManyToManyField(Pizza, through='PizzaOrder')
    date = models.DateField()
    open = models.BooleanField(default=True)

    def get_total_price(self):
        pizza_orders = self.pizzaorder_set.all()

        total = sum([pizza.get_price() for pizza in pizza_orders])
        return total


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza)
    debil = models.ForeignKey(Debil, verbose_name='déBIL')
    order = models.ForeignKey(Order)
    crust = models.ForeignKey(Crust, verbose_name='pâte')

    def get_price(self):
        return self.pizza.price + self.crust.overprice

    def get_verbose_description(self):
        return "%s - pate %s " % (self.pizza.name, self.crust.name)


class Payment(models.Model):
    debil = models.ForeignKey(Debil, verbose_name='déBIL')
    price = models.FloatField()


from orders.signals import *
