from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input-login', 'placeholder': 'ФИО'})
        self.fields['address'].widget.attrs.update({'class': 'input-login', 'placeholder': 'Адрес доставки'})
        self.fields['phone'].widget.attrs.update({'class': 'input-login', 'placeholder': 'Номер телефона'})

    class Meta:
        model = Order
        fields = ['name','address','phone']
