from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone	# for "default" argument in DateTimeField
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Item(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=150, verbose_name=('Item Slug'), default=name)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	supplier = models.CharField(max_length=100, blank=True, null=True)

	in_stock = models.BooleanField(default=False)
	stock_quantity = models.IntegerField(default=0)

	#capital
	capital_price_per_piece = models.IntegerField(default=0)
	capital_price_bulk = models.IntegerField(default=0)

	#selling prices
	discount = models.IntegerField(default=10)
	sell_price_retail= models.IntegerField(default=0)
	### find a way to automatically apply discounted prices


	notes = models.TextField(max_length=255, blank=True)


	## for this count update approach, see https://stackoverflow.com/questions/26285194/count-field-in-django
	# count = models.IntegerField(default=0)
	# quantity = Entity.objects.filter(pk=self.pk)     # Note: This does not fetch!
	# item_quantity.update(count=F('count')+1)              # Single SQL update statement

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'slug': self.slug})

	## thumbnail-related stuffs
	def thumbnail_directory(instance, filename):
		return 'users/{}/item_images/{}/{}'.format(instance.owner.username, instance.name, filename)
	thumbnail_image = models.ImageField(null=True, blank=True, upload_to=thumbnail_directory)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Item, self).save(*args, **kwargs)
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
