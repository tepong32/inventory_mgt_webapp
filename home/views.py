from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Item
from django.contrib.auth.models import User


# @login_required
def home(request):
	user = User
	items = Item.objects.all().order_by('name')
	context = {
		'items': items,
		'user': user,
	}
	return render(request, 'home/index.html', context)