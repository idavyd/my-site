from django import forms

from .models import Product, DroneProduct


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = DroneProduct
#         fields = [
#             'brand',
#             'model_name',
#             'price',
#             'description'
#         ]


class RawProductFrom(forms.Form):
    brand = forms.CharField()
    model_name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()