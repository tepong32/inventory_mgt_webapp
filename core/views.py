from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import AddPurchaseItemForm, AddSellItemForm


# class-based views
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .models import PurchaseItem, SellItem



# @login_required
class DashboardView(ListView):
	# context_object_name = 'Items'
	queryset = PurchaseItem.objects.all()
	template_name = 'core/dashboard.html'
	ordering = 'name'	# see if this works as an alphabetical filter
	paginate_by = 15

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)
		# '''
		# 	This function was used to override the "context" variable on the class-based view.
		# 	Think of this as a way of doing 
		# 	context = { 'xxx': xxx.objects.all(),
		# 				'yyy': yyy.objects.all()
		# 				}
		# 	in a function-based view.
		# '''
		# context['entertainment'] = Item.objects.filter(tag="Entertainment").order_by('-date_posted')
		# context['help'] = Item.objects.filter(tag="Help!").order_by('-date_posted')
		# context['hobby'] = Item.objects.filter(tag="Hobby").order_by('-date_posted')
		# context['jokes'] = Item.objects.filter(tag="Jokes").order_by('-date_posted')
		# context['school'] = Item.objects.filter(tag="School").order_by('-date_posted')
		# context['social'] = Item.objects.filter(tag="Social").order_by('-date_posted')

		context['purchaseItems'] = PurchaseItem.objects.all()
		context['sellItems'] = SellItem.objects.all()
		return context



### PURCHASE
class PurchaseItemCreateView(LoginRequiredMixin, CreateView):		
	model = PurchaseItem
	form_class = AddPurchaseItemForm
	template_name = 'core/itemCreate.html'
	success_message = "Item successfully added to list."
	success_url = '/'		# using this takes the user to a specific page after posting instead of the item detail page

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)


class PurchaseItemDetailView(DetailView):
	model = PurchaseItem
	template_name = 'core/itemDetail.html'
	purchaseItems = PurchaseItem.objects.all()
	context = {
		'purchaseItems': purchaseItems
	}


class PurchaseItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = PurchaseItem 
	form_class = AddPurchaseItemForm	# forumPostForm was the one used in the tutorials
	template_name = 'core/itemUpdate.html'
	success_message = "Item details updated"
	success_url = '/'

	def form_valid(self, form):			
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


class PurchaseItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = PurchaseItem
	template_name = 'core/itemConfirmDelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


### SELL
class SellItemCreateView(LoginRequiredMixin, CreateView):		
	model = SellItem
	form_class = AddSellItemForm
	template_name = 'core/itemCreate.html'
	success_message = "Item successfully added to list."
	success_url = '/'		# using this takes the user to a specific page after posting instead of the item detail page

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)


class SellItemDetailView(DetailView):
	model = SellItem
	template_name = 'core/itemDetail.html'
	sellItems = SellItem.objects.all()
	context = {
		'sellItems': sellItems,
	}

class SellItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = SellItem 
	form_class = AddSellItemForm	# forumPostForm was the one used in the tutorials
	template_name = 'core/itemUpdate.html'
	success_message = "Item details updated"
	success_url = '/'

	def form_valid(self, form):			
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


class SellItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = SellItem
	template_name = 'core/itemConfirmDelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False