from django.shortcuts import render
from django.conf import settings
from . import forms
# Create your views here.

def home(request):
    data = {
        'forms': forms.PersonForm
    }
    return render(request, 'index.html', data)
