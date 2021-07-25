from django import forms
from django.forms import fields
from .models import Student
from django.db.models.base import Model

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= "__all__"