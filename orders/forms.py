from django.forms import ModelForm
from orders.models import PizzaOrder


class PizzaOrderForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['debil', 'pizza', 'crust']
