from django.contrib import admin
from orders.models import Company, Bilien, Pizza, Order, PizzaBilienOrder


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Company, CompanyAdmin)


class BilienAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company')

admin.site.register(Bilien, BilienAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price')

admin.site.register(Pizza, PizzaAdmin)


class PizzaBilienOrderInline(admin.TabularInline):
    model = PizzaBilienOrder
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = (PizzaBilienOrderInline,)

admin.site.register(Order, OrderAdmin)
