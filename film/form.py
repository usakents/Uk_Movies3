from crispy_forms.helper import FormHelper
from django.db.models.base import Model
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from .models import(Register_users,Movies,Series,Carousel)

# class Register_userForm(forms.ModelForm):


#     class Meta:
#         model = Register_users
#         fields = '__all__'
#     def __init__(self, *args, **kwargs):
#         super(Register_userForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()   
     
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	user.contact = self.cleaned_data['contact']
	# 	if commit:
	# 		user.save()
	# 	return user