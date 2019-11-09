from django import forms
from django_countries.widgets import CountrySelectWidget
from . import models

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ('name', 'country')
        widgets = {'country': CountrySelectWidget()}