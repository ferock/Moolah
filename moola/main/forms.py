from django.contrib.auth.models import User
from django import forms

class registerForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','email','password')
		


class loginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password')
