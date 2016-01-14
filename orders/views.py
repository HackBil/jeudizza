from django.shortcuts import render
from django.db.models import Count, Sum
from orders.models import Order, PizzaOrder, Debil
from orders.forms import PizzaOrderForm
from orders.signals import INVITED_PREFIX

from operator import itemgetter
import random

WALKERS = 2


def home(request):
    pizza_count = PizzaOrder.objects.count()
    top5_pizzas = PizzaOrder.objects.values('pizza__name').annotate(count=Count('pizza__name')).order_by("-count")[:5]
    top5_debils = PizzaOrder.objects.values('debil__name').exclude(debil__name__startswith=INVITED_PREFIX).annotate(count=Count('debil__name')).order_by("-count")[:10]
    top_crusts = PizzaOrder.objects.values('crust__name').annotate(count=Count('crust__name')).order_by("-count")
    total_money = PizzaOrder.objects.all().aggregate(sum=Sum('pizza__price'))

    for debil in top5_debils:
        pizzas = PizzaOrder.objects.filter(debil__name=debil['debil__name']).values('pizza__name').annotate(count=Count('pizza__name')).order_by("-count")[:3]

        favorite_pizzas = [pizza['pizza__name'] for pizza in pizzas if int(pizza['count'] / debil['count'] * 100) > 20]

        debil['favorite'] = ''
        if not len(favorite_pizzas):
            debil['favorite'] = 'Indécis ! (' + debil['debil__name'] + ' mange trop de pizzas différentes)'
        else:
            if len(favorite_pizzas) > 1:
                debil['favorite'] += ', '.join(favorite_pizzas[:-1]) + ' et '
            if len(favorite_pizzas):
                debil['favorite'] += favorite_pizzas[-1]
        debil['comment'] = str(debil['count']) + ' pizzas'

    crust_comments = []
    crusts = [
        {
            'name': 'Classique',
            'message': 'sont des vrais qui ont plus tendance à prendre des pizzas avec pâte classique.'
        },
        {
            'name': 'Fine',
            'message': 'sont des faibles qui ont plus tendance à prendre des pizzas avec pâte fine.'
        }
    ]
    for crust in crusts:
        top_crust = PizzaOrder.objects.filter(crust__name=crust['name']).values('debil__name').exclude(debil__name__startswith=INVITED_PREFIX).annotate(count=Count('debil__name')).order_by('-count')[:5]
        top_crust = [pizza['debil__name'] for pizza in top_crust]

        crust_comment = ''
        if len(top_crust) > 1:
            crust_comment += ', '.join(top_crust[:-1]) + ' et '
        if len(top_crust):
            crust_comment += top_crust[-1]
        if crust_comment:
            crust_comment += ' ' + crust['message']
        crust_comments.append(crust_comment)

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

    availabe_people = last_order.pizzaorder_set.all().values_list('debil').distinct().count()
    if availabe_people < 4:
        return render(request, 'who-work-today.html', {'not_enough_people': True})

    random.seed(last_order.pk)

    # Pick the commander
    # We're not using .order_by('?').first() because que want to use seeded random
    eligible_commanders = list(Debil.objects.filter(pizzaorder__order=last_order).exclude(name__startswith=INVITED_PREFIX))
    commander = eligible_commanders[random.randint(0, len(eligible_commanders) - 1)]

    eligible_walkers = list(Debil.objects.filter(pizzaorder__order=last_order).exclude(pk=commander.pk).distinct())

    # Pick walkers
    walkers = []
    for x in range(0, WALKERS):
        index = random.randrange(len(eligible_walkers))
        walkers.append(eligible_walkers.pop(index))

    eligible_trashmans = list(Debil.objects.filter(pizzaorder__order=last_order).exclude(pk=commander.pk).exclude(pk__in=[walker.pk for walker in walkers]))
    trashman = eligible_trashmans[random.randint(0, len(eligible_trashmans) - 1)]

    return render(request, 'who-work-today.html', locals())


def argent(request):
    debils = Debil.objects.filter(disabled=False)
    return render(request, 'argent.html', locals())
