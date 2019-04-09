from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserRegisterationForm(forms.Form):
	username = forms.CharField(label = "Username")

	email = forms.EmailField(label = "Email")
	
	password = forms.CharField()



class LoginForm(forms.Form):
	username = forms.CharField(label = "Username")
	password = forms.CharField(label = "password")

