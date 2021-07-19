from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product, Service, PurchaseProduct
from django.contrib.auth.models import User


@login_required
def home(request):
	user = User
	products = Product.objects.all().order_by('name')
	services = Service.objects.all().order_by('name')
	context = {
		'products': products,
		'services': services,
		'user': user,
	}






	return render(request, 'home/index.html', context)