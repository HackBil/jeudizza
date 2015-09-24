from django.shortcuts import render
from orders.models import Order, PizzaOrder, Debil
from orders.forms import PizzaOrderForm
from orders.signals import INVITED_PREFIX

from operator import itemgetter
import random

WALKERS = 2


def home(request):
    pizza_count = PizzaOrder.objects.count()
    return render(request, 'index.html', locals())


def order(request):
    if request.method == 'POST':
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
    # last 5 orders
    last_orders = list(Order.objects.all().order_by('-date'))[:5]

    to_return = []

    for order in last_orders:
        pizza_orders = order.pizzaorder_set.all()

        treated_pizzas_orders = []
        formatted_order = []

        for pizza_order in pizza_orders:
            if pizza_order not in treated_pizzas_orders:
                treated_pizzas_orders.append(pizza_order)
                same_pizzas = []
                debil_list = [pizza_order.debil.name]
                for other_pizza_order in pizza_orders:
                    if other_pizza_order not in treated_pizzas_orders and other_pizza_order.get_verbose_description() == pizza_order.get_verbose_description():
                        treated_pizzas_orders.append(other_pizza_order)
                        same_pizzas.append(other_pizza_order)
                        debil_list.append(other_pizza_order.debil.name)
                quantity = 1 + len(same_pizzas)
                formatted_order.append({
                    "quantity": quantity,
                    "pizza": pizza_order,
                    "price": pizza_order.get_price() * quantity,
                    "debil_list": debil_list
                })
                formatted_order = sorted(formatted_order, key=itemgetter('quantity'), reverse=True)
        to_return.append({"content": formatted_order,
                          "info": order})

    return render(request, 'orders-history.html', {"last_orders": to_return})


def who_work_today(request):
    last_order = Order.objects.all().order_by('pk').last()

    random.seed(last_order)

    eligible_walkers = list(Debil.objects.filter(pizzaorder__order=last_order))

    # Pick walkers
    walkers = []
    for x in range(0, WALKERS):
        index = random.randrange(len(eligible_walkers))
        walkers.append(eligible_walkers.pop(index))

    eligible_commanders = list(
        Debil.objects
        .filter(pizzaorder__order=last_order)
        .exclude(name__startswith=INVITED_PREFIX)
        .exclude(name__in=[walker.name for walker in walkers])
    )
    # Pick the commander
    index = random.randrange(len(eligible_commanders))
    commander = eligible_commanders.pop(index)

    return render(request, 'who-work-today.html', locals())


def argent(request):
    debils = Debil.objects.all()



    return render(request, 'argent.html', locals())
