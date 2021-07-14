from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	'''
		these fields take arguments (required=true/false).
		by default, required=true
	'''
	# add fields to this form
	email = forms.EmailField() 

	class Meta:
		model = User 	# the mode that is going to be affected is the User model
		fields = ["username", "email", "password1", "password2", ]


# after adding these forms, add it to the views.py
class UserUpdateForm(forms.ModelForm):
	'''
		these fields take arguments (required=true/false).
		by default, required=true
	'''
	email = forms.EmailField()

	class Meta:
		model = User 	# the model that is going to be affected is the User model, 
		fields = ["email"]	# hence its attributes are the ones in this "fields" variable // "username" field removed


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile 	# the model that is going to be affected by this form is the Profile model,
		fields = ["display_name", "image", "gender", "location", "quote", "about_me",]

		'''
			I removed these fields because they're also removed/commented-out from the Profile model.
			Uncomment them from the model, modify as needed, run migrations and then add them to the fields attribute of this form...if you want to.
		'''
		# "google", "linkedin", "github", "facebook", "twitter", "instagram", "school", "course", "year_in_school",
		# "user_group" field was not included for it will determine ranks in the future
		# "reach_me_intro", "profile_snippet" were not included due to redunduncy // just used "about_me" in its place on home_unauthed/home_unauthed.html
