from django import forms
from .models import Item, PurchaseItem, SellItem, Category


'''
    If we need a dynamic Category objects list, we will implement these commented-out
    lines. However, since we only have a fixed two-option field for purchase_type and
    sell_type, I just hard-coded those options inside the Model.

    Should we decide to use this dynamic method, we still need to comment these lines
    out on the first "makemigrations" command. Also, the server needs to be restarted
    everytime instances of the Category class are added for them to be reflected as 
    options on the form field.
'''

# categories = Category.objects.all().values_list('name', 'name')
# categories_list = []

# for item in categories:
#     categories_list.append(item)

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'supplier']

        
class AddPurchaseItemForm(forms.ModelForm):

    class Meta:
        model = PurchaseItem
        fields = "__all__"
        exclude = ['tag']
        # widgets = {
        #     'purchase_type' : forms.Select(choices=categories, attrs={'class': 'form-control'})
        # }


class AddSellItemForm(forms.ModelForm):

    class Meta:
        model = SellItem
        fields = "__all__"
        exclude = ['tag']
        # widgets = {
        #     'sell_type' : forms.Select(choices=categories, attrs={'class': 'form-control'})
        # }
