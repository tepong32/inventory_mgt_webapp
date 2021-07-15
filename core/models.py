from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.functions import Lower


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name.title() # '.title()' to turn them all-caps


class Item(models.Model):
	'''
	General attributes of each item.
	This will just be the base-class where PurchaseItem and SellItem inherits their attributes.
	No need to create actual instances.
	'''
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	supplier = models.CharField(max_length=100, default="---")
	slug = models.SlugField(max_length=150, verbose_name=('Item Slug'), default=name)
	
	# these should be defined inside the view
	# def invested_capital(self):
	# 	purchase_list = []

	# def gross_profit(self):
	# 	sell_list = []

	### important model defaults // modify as needed
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail-item', kwargs={'slug': self.slug})
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.name = self.name.title()
		super(Item, self).save(*args, **kwargs)


class PurchaseItem(Item):
	'''
	Purchases details here
	'''
	tag = models.CharField(max_length=10, default='purchase')	# placeholder / used for filtering 
	purchase_date = models.DateField()
	RETAIL = 'Retail'
	WHOLESALE = 'Wholesale'
	purchase_type_choices = (
		(RETAIL, 'retail'),
		(WHOLESALE, 'wholesale')
		)
	purchase_type = models.CharField(
        max_length=10,
        choices=purchase_type_choices,
        default=RETAIL,
    )
	purchase_type = models.CharField(max_length=10, default='wholesale')
	r_purchase_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	w_purchase_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	purchased_qty = models.IntegerField(default=0)
	purchase_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	def total_capital(self):
		return int(self.purchase_price * self.purchased_qty)
	notes = models.TextField(max_length=255, blank=True)

	### important model defaults // modify as needed
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail-purchase', kwargs={'slug': self.slug})
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name + " " + str(self.purchase_date))
		self.name = self.name.title()
		super(PurchaseItem, self).save(*args, **kwargs)


class SellItem(Item):
	'''
	Selling details here
	'''
	tag = models.CharField(max_length=10, default='sell')
	sell_date = models.DateField()
	RETAIL = 'Retail'
	WHOLESALE = 'Wholesale'
	sell_type_choices = (
		(RETAIL, 'retail'),
		(WHOLESALE, 'wholesale')
		)
	sell_type = models.CharField(
        max_length=10,
        choices=sell_type_choices,
        default=RETAIL,
    )
	sell_type = models.CharField(max_length=10)
	r_sell_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	w_sell_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	sold_qty = models.IntegerField(default=0)
	selling_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	def total_sales(self):
		return int(self.sell_price * self.sold_qty)
	notes = models.TextField(max_length=255, blank=True)

	### important model defaults // modify as needed
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail-sell', kwargs={'slug': self.slug})
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name + " " + str(self.sell_date))
		self.name = self.name.title()
		super(SellItem, self).save(*args, **kwargs)
