from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import PurchaseItem, SellItem
from django.contrib.auth.models import User


@login_required
def home(request):
	user = User
	purchaseItems = PurchaseItem.objects.all().order_by('purchase_date')
	sellItems = SellItem.objects.all().order_by('-sell_date')
	context = {
		'purchaseItems': purchaseItems,
		'sellItems': sellItems,
		'user': user,
	}






	return render(request, 'home/index.html', context)