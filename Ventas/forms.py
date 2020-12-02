from django import forms
from .models import Order, Product
from django.contrib.admin import widgets


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'is_glasses',)
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'is_glasses': '¿Es Lente?',
        }
        widgets = {
            'description':forms.TextInput(attrs={'required': False}),
        }


class ProductGlassesForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price',
                  'is_glasses', 'distance', 'side', 'frame',)
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'is_glasses': '¿Es Lente?',
            'distance': 'Distancia',
            'side': 'Lado',
            'frame': '¿Incluye Armazón?',
        }
        widgets = {
            'distance':forms.Select(),
            'side':forms.Select(),
            'description':forms.TextInput(attrs={'required': False}),
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('client', 'article', 'units', 'status',)
        labels = {
            'client': 'Cliente',
            'article': 'Artículo',
            'units': 'Cantidad',
            'status': 'Estado',
        }
        widgets = {
            'client':forms.Select(),
            'article':forms.Select(),
            'status':forms.Select(),
        }

