from django.contrib import admin
from .models import PurchaseItem, SellItem, Category

# Register your models here.
admin.site.register(PurchaseItem)
admin.site.register(SellItem)
admin.site.register(Category)

