from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@.com'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }