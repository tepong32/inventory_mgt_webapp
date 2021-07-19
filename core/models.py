from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.functions import Lower



class Product(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=150, verbose_name=('entry slug'), default=name)
	RETAIL = 'retail'
	WHOLESALE = 'wholesale'
	CUSTOM = 'custom-wholesale'
	r_or_w_choices = (
		(RETAIL, 'retail'),
		(WHOLESALE, 'wholesale'),
		(CUSTOM, 'custom-wholesale'),
	)
	product_type = models.CharField(
        max_length=10,
        choices=r_or_w_choices,
        default=RETAIL, help_text='No discount = Retail, Percentage-based discount = Wholesale, Custom discount = Custom'
    )

	def __str__(self):
		return self.name.title()
	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'slug': self.slug})
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name + '-' + self.product_type)
		super(Product, self).save(*args, **kwargs)


class PurchaseProduct(models.Model):
	'''
	General attributes of each  Purchase entry based on the Product class.
	'''
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date = models.DateField()
	qty = models.IntegerField(default=0)
	slug = models.CharField(max_length=50, blank=True)
	

	# automatically determines the purchase price based on whether the purchase was retail or wholesale
	#retail
	r_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	#wholesale
	w_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	w_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	#custom
	c_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	c_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")

	def total_capital(self):
		if self.product_type == 'RETAIL':
			return int(self.r_price * self.qty)
		elif self.product_type == 'WHOLESALE':
			return int(self.w_price * self.w_discount * self.qty)
		else:
			return int(self.c_price * self.qty - self.c_discount)


	supplier = models.CharField(max_length=100, default="---")
	notes = models.TextField(max_length=255, blank=True)

	def __str__(self):
		return str(self.name.title() + '-' + str(self.date) + '-purchase')

	def get_absolute_url(self):
		return reverse('ppurchase-detail', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.product.name + '-' + str(self.date))
		super(PurchaseProduct, self).save(*args, **kwargs)
	
	

class SellProduct(models.Model):
	'''
		General attributes of each  Sell entry based on the Product class.
	'''
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date = models.DateField()
	qty = models.IntegerField(default=0)

	# automatically determines the purchase price based on whether the purchase was retail or wholesale
	#retail
	r_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	#wholesale
	w_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	w_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	#custom
	c_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	c_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")

	def total_sales(self):
		if self.product_type == 'RETAIL':
			return int(self.r_price * self.qty)
		elif self.product_type == 'WHOLESALE':
			return int(self.w_price * self.w_discount * self.qty)
		else:
			return int(self.c_price * self.qty - self.c_discount)


	notes = models.TextField(max_length=255, blank=True)

	### important model defaults // modify as needed
	def __str__(self):
		return str(self.name.title() + '-' + self.date + '-sell')





class Service(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=150, verbose_name=('entry slug'), default=name)


	def __str__(self):
		return self.name.title()
	def get_absolute_url(self):
		return reverse('service-detail', kwargs={'slug': self.slug})
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		super(Service, self).save(*args, **kwargs)


class PurchaseService(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	date = models.DateField()
	price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	qty = models.IntegerField(default=1)

	def total_capital(self):
		return set(self.price * self.qty)

	def __str__(self):
		return str(self.name.title() + '-' + self.date + '-purchase')
		

class SellService(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	date = models.DateField()
	price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	qty = models.IntegerField(default=1)


	def __str__(self):
		return str(self.name.title() + '-' + self.date + '-purchase')