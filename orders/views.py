from django.shortcuts import render
from orders.models import Order, PizzaOrder
from orders.forms import PizzaOrderForm


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

    # GET form
    form = PizzaOrderForm()

    return render(request, 'order.html', {'form': form})


def orders_history(request):
    last_orders = list(Order.objects.all().order_by('-date'))[-5:]
    return render(request, 'orders-history.html', locals())
