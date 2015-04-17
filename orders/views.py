from django.shortcuts import render
from orders.models import Order


def orders(request):
    last_orders = list(Order.objects.all().order_by('-date'))[-5:]
    return render(request, 'orders.html', locals())
