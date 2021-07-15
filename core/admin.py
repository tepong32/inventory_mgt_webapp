from django.contrib import admin
from .models import Item, PurchaseItem, SellItem, Category

# Register your models here.
admin.site.register(Item)
admin.site.register(PurchaseItem)
admin.site.register(SellItem)
admin.site.register(Category)

