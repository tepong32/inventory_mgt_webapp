from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import AddProductForm, PurchaseProductForm 


# generic class-based views where we get inheritance from
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)

from .models import (
	Product,
	PurchaseProduct,
	SellProduct,
	Service,
	PurchaseService,
	SellService
	) # or 'import *'




# @login_required
class DashboardView(ListView):
	# context_object_name = 'Items'
	queryset = Product.objects.all()
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

		context['products'] = Product.objects.all()
		context['services'] = Service.objects.all()

		return context

### PRODUCT
class ProductDetailView(DetailView):
	model = Product
	template_name = 'core/productDetail.html'
	# pproducts = PurchaseProduct.objects.all()
	# context = {
	# 	'pproducts': pproducts
	# }

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
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

		context['ppurchases'] = PurchaseProduct.objects.all()
		context['psells'] = SellProduct.objects.all()

		return context
		
from sweetify.views import SweetifySuccessMixin
class ProductCreateView(LoginRequiredMixin, SweetifySuccessMixin, CreateView):
	model = Product
	form_class = AddProductForm
	template_name = 'core/addProduct.html'
	success_message = 'Entry created'
	# success_url = '/'

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product 
	form_class = AddProductForm
	template_name = 'core/updateProduct.html'
	success_message = "Product updated"
	# success_url = '/'

	def form_valid(self, form):			
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Product
	template_name = 'core/confirmProductDelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False



# product purchases
class AddPPurchase(LoginRequiredMixin, CreateView):		
	model = PurchaseProduct
	form_class = PurchaseProductForm
	template_name = 'core/addPPurchase.html'
	success_message = "Line entry added"
	success_url = '/'

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)

class PPurchaseDetail(DetailView):
	model = PurchaseProduct
	template_name = 'core/pproductDetail.html'
	pproducts = PurchaseProduct.objects.all()
	context = {
		'pproducts': pproducts
	}

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['ppurchases'] = PurchaseProduct.objects.all()
		context['psells'] = SellProduct.objects.all()

		return context

class UpdatePPurchase(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = PurchaseProduct 
	form_class = AddProductForm
	template_name = 'core/updatePPurchase.html'
	success_message = "Product updated"
	# success_url = '/'

	def form_valid(self, form):			
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


class DeletePPurchase(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = PurchaseProduct
	template_name = 'core/confirmProductDelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


# product sells
class AddPSell(LoginRequiredMixin, CreateView):		
	model = SellProduct
	form_class = PurchaseProductForm
	template_name = 'core/addPSell.html'
	success_message = "Line entry added"
	# success_url = '/'

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)

class UpdatePSell(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = SellProduct 
	form_class = AddProductForm
	template_name = 'core/updatePSell.html'
	success_message = "Product updated"
	# success_url = '/'

	def form_valid(self, form):			
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


class DeletePSell(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = SellProduct
	template_name = 'core/confirmProductDelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False

