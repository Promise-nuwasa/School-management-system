from django import forms
from django.forms import fields
from .models import Events
from django.db.models.base import Model

class EventsRegistrationForm(forms.ModelForm):
    class Meta:
        model= Events
        fields= "__all__"