# -*- coding: utf-8 -*-
from django.contrib import admin
from orders.models import Company, Debil, Pizza, Crust, Order, PizzaOrder


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Company, CompanyAdmin)


class CrustAdmin(admin.ModelAdmin):
    list_display = ('name', 'overprice')

admin.site.register(Crust, CrustAdmin)


class DebilAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

admin.site.register(Debil, DebilAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price')

admin.site.register(Pizza, PizzaAdmin)


class PizzaOrderInline(admin.TabularInline):
    model = PizzaOrder
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'open')
    inlines = (PizzaOrderInline,)

admin.site.register(Order, OrderAdmin)
