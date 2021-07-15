from django import forms
from .models import PurchaseItem, SellItem, Category



categories = Category.objects.all().values_list('name', 'name')
categories_list = []

for item in categories:
    categories_list.append(item)


class AddPurchaseItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model?

    class Meta:
        model = PurchaseItem
        fields = "__all__"
        exclude = ['owner', 'slug',]
        widgets = {
            'purchase_type' : forms.Select(choices=categories, attrs={'class': 'form-control'})
        }


class AddSellItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = SellItem
        fields = "__all__"
        exclude = ['owner', 'slug', ]
        widgets = {
            'sell_type' : forms.Select(choices=categories, attrs={'class': 'form-control'})
        }
