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
    list_display = ('name', 'company', 'solde', 'disabled')
    actions = ('disable',)

    def solde(self, obj):
        return obj.get_solde()

    def disable(self, request, queryset):
        for debil in queryset:
            debil.disabled = True
            debil.save()
        return

admin.site.register(Debil, DebilAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price', 'available', 'calories')

admin.site.register(Pizza, PizzaAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('debil', 'price', 'date')

admin.site.register(Payment, PaymentAdmin)


class PizzaOrderInline(admin.TabularInline):
    model = PizzaOrder
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'open')
    inlines = (PizzaOrderInline,)

admin.site.register(Order, OrderAdmin)


class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ('debil', 'pizza', 'crust', 'order')

admin.site.register(PizzaOrder, PizzaOrderAdmin)
