from django.forms import ModelForm
from orders.models import PizzaOrder, Debil, Pizza, CrepeOrder


class PizzaOrderForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['debil', 'pizza', 'crust']

    def __init__(self, *args, **kwargs):
        super(PizzaOrderForm, self).__init__(*args, **kwargs)

        self.fields["debil"].queryset = Debil.objects.filter(disabled=False)
        self.fields["pizza"].queryset = Pizza.objects.filter(available=True)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CrepeOrderForm(ModelForm):
    class Meta:
        model = CrepeOrder
        fields = ['debil_set']

    def __init__(self, *args, **kwargs):
        super(CrepeOrderForm, self).__init__(*args, **kwargs)

        self.fields["debil_set"].queryset = Debil.objects.filter(disabled=False)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
