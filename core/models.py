from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone	# for "default" argument in DateTimeField
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.functions import Lower

### PURCHASE
class PurchaseItem(models.Model):
	# general/universal item info
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, verbose_name=('Item Slug'), default=name)
	supplier = models.CharField(max_length=100, default="---")

	### PURCHASE details
	purchase_date = models.DateField(help_text="mm/dd/yyyy")
	retail = 'Retail'
	wholesale = 'Wholesale'
	purchase_type_choices = (
		(retail, 'retail'),
		(wholesale, 'wholesale')
		)
	purchase_type = models.CharField(
        max_length=10,
        choices=purchase_type_choices,
        default=wholesale,
    )
	purchase_type = models.CharField(max_length=10, default='wholesale')
	purchase_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
	purchased_qty = models.IntegerField(default=0)
	purchase_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	def total_capital(self):
		return int(self.purchase_price * self.purchased_qty)

	notes = models.TextField(max_length=255, blank=True)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail-purchase', kwargs={'slug': self.slug})
	## thumbnail-related stuffs
	def thumbnail_directory(instance, filename):
		return 'users/{}/item_images/{}/{}'.format(instance.owner.username, instance.name, filename)
	thumbnail_image = models.ImageField(null=True, blank=True, upload_to=thumbnail_directory)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name + " " + str(self.purchase_date))
		self.name = self.name.title()
		super(PurchaseItem, self).save(*args, **kwargs)
		# downsizing header_image, if there's any
		if self.thumbnail_image:
			thumbnail_img = Image.open(self.thumbnail_image.path)			# open the image of the current instance
			if thumbnail_img.height > 700 or thumbnail_img.width > 700:		# for sizing-down the images to conserve memory in the server
				output_size = (700, 700)
				thumbnail_img.thumbnail(output_size)
				thumbnail_img.save(self.thumbnail_image.path)


### SELL
class SellItem(models.Model):
	# general/universal item info
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, verbose_name=('Item Slug'), default=name)
	sold_to = models.CharField(max_length=100, default="---")

	### SELL details
	sell_date = models.DateField()
	retail = 'Retail'
	wholesale = 'Wholesale'
	sell_type_choices = (
		(retail, 'retail'),
		(wholesale, 'wholesale')
		)
	sell_type = models.CharField(
        max_length=10,
        choices=sell_type_choices,
        default=wholesale,
    )
	sell_type = models.CharField(max_length=10)
	sell_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	sold_qty = models.IntegerField(default=0)
	selling_discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, help_text="Ex: 10.5% discount = 0.105")
	def total_sales(self):
		return int(self.sell_price * self.sold_qty)


	# def on_hand(self):
	# 	return int(self.purchased_qty - self.sold_qty)


	notes = models.TextField(max_length=255, blank=True)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail-sell', kwargs={'slug': self.slug})
	## thumbnail-related stuffs
	def thumbnail_directory(instance, filename):
		return 'users/{}/item_images/{}/{}'.format(instance.owner.username, instance.name, filename)
	thumbnail_image = models.ImageField(null=True, blank=True, upload_to=thumbnail_directory)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name + " " + str(self.sell_date))
		self.name = self.name.title()
		super(SellItem, self).save(*args, **kwargs)
		# downsizing header_image, if there's any
		if self.thumbnail_image:
			thumbnail_img = Image.open(self.thumbnail_image.path)			# open the image of the current instance
			if thumbnail_img.height > 700 or thumbnail_img.width > 700:		# for sizing-down the images to conserve memory in the server
				output_size = (700, 700)
				thumbnail_img.thumbnail(output_size)
				thumbnail_img.save(self.thumbnail_image.path)


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name.title() # '.title()' to turn them all-caps
