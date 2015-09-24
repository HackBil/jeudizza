from django.forms import ModelForm
from orders.models import PizzaOrder


class PizzaOrderForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['debil', 'pizza', 'crust']

    def __init__(self, *args, **kwargs):
        super(PizzaOrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
