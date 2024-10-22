from django import forms

from .models import Product, DroneProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = DroneProduct
        fields = [
            'brand',
            'model_name',
            'price',
            'description'
        ]

class RawProductFrom(forms.Form):
    name = forms.CharField()
    overview = forms.CharField()
    price = forms.DecimalField(initial=199.99)
    # comment
    # my new comment