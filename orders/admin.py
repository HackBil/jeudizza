from django.conf.urls import patterns
from django.shortcuts import render
from django.contrib import admin

from orders.models import Company, Debil, Pizza, Crust, Order, PizzaOrder, Payment


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Company, CompanyAdmin)


class CrustAdmin(admin.ModelAdmin):
    list_display = ('name', 'overprice')

admin.site.register(Crust, CrustAdmin)


class DebilAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'solde')

    def solde(self, obj):
        return obj.get_solde()

admin.site.register(Debil, DebilAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price')

admin.site.register(Pizza, PizzaAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('debil', 'price')

admin.site.register(Payment, PaymentAdmin)


class PizzaOrderInline(admin.TabularInline):
    model = PizzaOrder
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'open')
    inlines = (PizzaOrderInline,)

admin.site.register(Order, OrderAdmin)


def payments(request):
    debils = Debil.objects.all()
    last_orders = list(Order.objects.all().order_by('-date'))[:5]

    return render(
        request,
        'payments.html',
        {
            'debils': debils,
            'last_orders': last_orders
        }
    )


def pay_order(request):
    saved = False
    if request.method == 'POST':
        debil = Debil.objects.get(pk=request.POST.get('debil'))
        order = Order.objects.get(pk=request.POST.get('order'))
        Payment(debil=debil, price=order.get_total_price()).save()
        saved = True

    debils = Debil.objects.all()
    last_orders = list(Order.objects.all().order_by('-date'))[:5]

    return render(
        request,
        'payments.html',
        {
            'debils': debils,
            'last_orders': last_orders,
            'saved': saved
        }
    )


def pay_debil(request):
    saved = False
    if request.method == 'POST':
        giver = Debil.objects.get(pk=request.POST.get('giver'))
        taker = Debil.objects.get(pk=request.POST.get('taker'))
        price = request.POST.get('price')
        print(price)
        Payment(debil=giver, price=float(price)).save()
        Payment(debil=taker, price=-float(price)).save()
        saved = True

    debils = Debil.objects.all()
    last_orders = list(Order.objects.all().order_by('-date'))[:5]

    return render(
        request,
        'payments.html',
        {
            'debils': debils,
            'last_orders': last_orders,
            'saved': saved
        }
    )


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^payments/$', admin.site.admin_view(payments)),
            (r'^pay_debil/$', admin.site.admin_view(pay_debil)),
            (r'^pay_order/$', admin.site.admin_view(pay_order))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
