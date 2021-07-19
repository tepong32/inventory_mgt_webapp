from django import forms
from .models import (
    Product,
    PurchaseProduct,
    SellProduct,
    Service,
    PurchaseService,
    SellService
    ) # or 'import *'


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type']

        
class PurchaseProductForm(forms.ModelForm):

    class Meta:
        model = PurchaseProduct
        fields = "__all__"
        exclude = ['slug']


class SellProductForm(forms.ModelForm):

    class Meta:
        model = SellProduct
        fields = "__all__"

