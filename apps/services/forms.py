from django import forms
from .models import Service
from facilities.models import Facility

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility','name','description','category','skill_type']
