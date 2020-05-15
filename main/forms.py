from django import forms
from django.forms import ModelForm
from .models import *
from users import models


class LocationForm(forms.ModelForm):
    location = models.CharField(max_length=9, choices=LOCATION_OPTIONS, default='Home')

    class Meta:
        fields = '__all__'