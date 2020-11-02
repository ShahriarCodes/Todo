from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs = {'placeholder': 'This is the place for title placeholder'}),

        }
