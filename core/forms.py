from django import forms
from .models import Item


class AddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model?
    
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ['owner', 'slug', 'date_created', 'date_modified',]
    	# widgets = {
    	# 	'category' : forms.Select(choices=categories, attrs={'class': 'form-control'})
    	# }