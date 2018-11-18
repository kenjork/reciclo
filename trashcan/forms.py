from django import forms
from django.forms import ModelForm

from .models import TrashCan


class TrashCanForm(ModelForm):
    
    class Meta:
        model = TrashCan
        #fields = '__all__'
        exclude = (
            'recyclers',
        )