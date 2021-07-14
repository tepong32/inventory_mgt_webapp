from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import AddItemForm


# class-based views
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .models import Item



# @login_required
class DashboardView(ListView):
	context_object_name = 'Items'
	queryset = Item.objects.all()
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
		context['items'] = Item.objects.all()
		# and so on for more models
		return context


class ItemDetailView(DetailView):
	model = Item
	template_name = 'core/itemDetail.html'
	items = Item.objects.all()
	context = {
		'items': items
	}


class ItemCreateView(LoginRequiredMixin, CreateView):		
	model = Item
	form_class = AddItemForm
	template_name = 'core/itemCreate.html'
	success_message = "Item successfully added to list."
	success_url = '/items'		# using this takes the user to a specific page after posting instead of the item detail page

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the owner
		form.instance.owner = self.request.user 	# set the owner to the current logged-in user
		return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item 
	form_class = AddItemForm	# forumPostForm was the one used in the tutorials
	template_name = 'core/itemUpdate.html'
	success_message = "Item details updated"
	success_url = '/items'

	def form_valid(self, form):			
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Item
	template_name = 'core/itemConfirmDelete.html'
	success_url = '/items'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.owner:
			return True
		return False