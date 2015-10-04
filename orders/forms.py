from django.forms import ModelForm
from orders.models import PizzaOrder, Debil


class PizzaOrderForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['debil', 'pizza', 'crust']

    def __init__(self, *args, **kwargs):
        super(PizzaOrderForm, self).__init__(*args, **kwargs)

        self.fields["debil"].queryset = Debil.objects.filter(disabled=False)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
