from django import forms
from django.forms import ModelForm
from .models import DataModel

# Create the form class.
class ProfileForm(ModelForm):
	class Meta:
		model = DataModel
		fields = ('naziv', 'datoteka')