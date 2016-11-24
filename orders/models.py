from django.db import models
from django.db.models import Sum
from django.utils.safestring import mark_safe


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
        depts = self.dept_set.aggregate(Sum('amount')).get("amount__sum") or 0.0
        print("%s %f %f" % (self.name, paid, depts))
        return paid - depts


class Crust(models.Model):
    name = models.CharField(max_length=64, unique=True)
    overprice = models.FloatField(default=0)

    def __str__(self):
        if self.overprice == 0:
            return self.name
        else:
            return "%s (+%g€)" % (self.name, self.overprice)


class Pizza(models.Model):
    CALORIES_MAN = 2400
    CALORIES_WOMAN = 1800
    SEX_PARTY = 200
    HIGHEST_LENGTH = 32
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=256)
    price = models.FloatField(default=6)
    available = models.BooleanField(default=True)
    calories = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        space = "&nbsp;"
        return mark_safe("%s %s (%g€) | %s Cal | %2.0f%% H | %2.0f%% F | %2.0f soirées coquines" % (self.name, space * (self.HIGHEST_LENGTH - len(self.name)), self.price, self.calories, self.calories/self.CALORIES_MAN*100, self.calories/self.CALORIES_WOMAN*100, self.calories/self.SEX_PARTY))


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


class Dept(models.Model):
    debil = models.ForeignKey(Debil, verbose_name='déBIL')
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True, null=True)


class Payment(models.Model):
    debil = models.ForeignKey(Debil, verbose_name='déBIL')
    price = models.FloatField()
    date = models.DateField(auto_now_add=True, null=True)


class CrepeOrder(models.Model):
    debil_set = models.ManyToManyField(Debil, verbose_name='déBIL', related_name='crepeOrders', blank=True)
    date = models.DateField()
    price = models.FloatField(null=True, blank=True)
    open = models.BooleanField(default=True)

from orders.signals import *
