from django.contrib import admin
from .models import (
	Product,
	PurchaseProduct,
	SellProduct,
	Service,
	PurchaseService,
	SellService
	) # or 'import *'

# Register your models here.
admin.site.register(Product)
admin.site.register(PurchaseProduct)
admin.site.register(SellProduct)
admin.site.register(Service)
admin.site.register(PurchaseService)
admin.site.register(SellService)

