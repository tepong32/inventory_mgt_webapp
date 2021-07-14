from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField


'''
	README:
	This Profile model is an extension of from "django.contrib.auth.models.User". Browse into that directory and change the email attribute of 
	the AbstractUser class. Add "unique=True" to make sure that no email address can eb used to create multiple accounts.
	If you want to have more control over your user model, you can follow the model format below:
	https://github.com/mitchtabian/Codingwithmitch-Chat/blob/uploading-an-image/account/forms.py

	Full tutorial here: https://codingwithmitch.com/courses/real-time-chat-messenger/demo/

	P.S.: I get a couple of ideas on how to implement certain logic there. I just did not implement Javascripts because I don't understand it well at the time of writing this code.
'''

class Profile(models.Model):

	# profile-related stuffs 
	user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted, the profile will be deleted, too
	display_name = models.CharField(blank=True, null=True, max_length=50, unique=True, verbose_name="Display Name: ",help_text="Get a cool-sounding alias.") 
	Male = "Male"
	Female = "Female"
	Neutral = "Neutral"
	gender_choice = [
		(Male, "Male"),
		(Female, "Female"),
		(Neutral, "Neutral")
	]
	gender = models.CharField(
		max_length=10,
		choices=gender_choice,
		default=Neutral, verbose_name="Gender: "
	)
	location = models.CharField(blank=True, null=True, max_length=255, default="Uh...Earth?", verbose_name="Location: ", help_text="Do you want to fill this out? :D")

	# Other information that can be displayed on a user profile page:
	quote = models.CharField(blank=True, max_length=300, verbose_name="Quote you live by: ", help_text="'Pampa-Angas'")
	about_me = models.TextField(blank=True, default="...Default About Me text", help_text="Tell us something about you.")
	
	def dp_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP/<username>/<filename> ---check settings.py. MEDIA_ROOT=media for the exact folder/location
		return 'users/{}/DP/{}'.format(instance.user.username, filename)
	image = models.ImageField(default='defaults/round.png', blank=True, upload_to=dp_directory_path, verbose_name="Profile Picture: ", help_text='Help us recognize you. ;)')


	def __str__(self):
		return f"{self.user.username}"

	def get_absolute_url(self):
		return reverse('profile', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):		# for resizing/downsizing images
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)	# open the image of the current instance
		if img.height > 600 or img.width > 600:	# for sizing-down the images to conserve memory in the server
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)



# '''
# 	This is CodingwithMitch's user model modified to match Profile(above) a little bit.
# 	Doubting if I should use this instead of the above model.
# 	Referenc: https://github.com/mitchtabian/Codingwithmitch-Chat/blob/custom-user-model/account/models.py
# '''

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os


# class MyAccountManager(BaseUserManager):
# 	def create_user(self, email, username, password=None):
# 		if not email:
# 			raise ValueError('Users must have an email address')
# 		if not username:
# 			raise ValueError('Users must have a username')

# 		user = self.model(
# 			email=self.normalize_email(email),
# 			username=username,
# 		)

# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user

# 	def create_superuser(self, email, username, password):
# 		user = self.create_user(
# 			email=self.normalize_email(email),
# 			password=password,
# 			username=username,
# 		)
# 		user.is_admin = True
# 		user.is_staff = True
# 		user.is_superuser = True
# 		user.save(using=self._db)
# 		return user


# def get_profile_image_filepath(self, filename):
# 	return 'profile_images/' + str(self.pk) + '/profile_image.png'

# def get_default_profile_image():
# 	return "codingwithmitch/logo_1080_1080.png"


# class Profile(AbstractBaseUser):
# 	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
# 	username 				= models.CharField(max_length=30, unique=True)
# 	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
# 	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
# 	is_admin				= models.BooleanField(default=False)
# 	is_active				= models.BooleanField(default=True)
# 	is_staff				= models.BooleanField(default=False)
# 	is_superuser			= models.BooleanField(default=False)
# 	image					= models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
# 	hide_email				= models.BooleanField(default=True)

# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['username']

# 	objects = MyAccountManager()

# 	def __str__(self):
# 		return self.username

# 	def get_profile_image_filename(self):
# 		return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

# 	# For checking permissions. to keep it simple all admin have ALL permissons
# 	def has_perm(self, perm, obj=None):
# 		return self.is_admin

# 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# 	def has_module_perms(self, app_label):
# 		return True