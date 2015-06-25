# -*- coding: utf-8 -*-
from django.shortcuts import render
from orders.models import Order, PizzaOrder, Debil
from orders.forms import PizzaOrderForm
from orders.signals import INVITED_PREFIX


import random


WALKERS = 2


def home(request):
    pizza_count = PizzaOrder.objects.count()
    return render(request, 'index.html', locals())


def order(request):
    if(request.method == 'POST'):
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            PizzaOrder(
                debil=form.cleaned_data["debil"],
                pizza=form.cleaned_data["pizza"],
                crust=form.cleaned_data["crust"],
                order=Order.objects.get(open=True)
            ).save()
            return render(request, 'enjoy.html', {'form': form})
        else:
            return render(request, 'order.html', {'form': form})
    # GET
    form = PizzaOrderForm()

    return render(request, 'order.html', {'form': form})


def orders_history(request):
    last_orders = list(Order.objects.all().order_by('-date'))[:5]
    return render(request, 'orders-history.html', locals())


def who_work_today(request):
    last_order = Order.objects.all().order_by('pk').last()

    eligible_walkers = list(Debil.objects.filter(pizzaorder__order=last_order))

    # Pick walkers
    walkers = []
    for x in range(0, WALKERS):
        index = random.randrange(len(eligible_walkers))
        walkers.append(eligible_walkers.pop(index))

    eligible_commanders = list(Debil.objects.filter(pizzaorder__order=last_order).exclude(name__startswith=INVITED_PREFIX).exclude(name__in=[walker.name for walker in walkers]))

    # Pick the commander
    index = random.randrange(len(eligible_commanders))
    commander = eligible_commanders.pop(index)

    return render(request, 'who-work-today.html', locals())
