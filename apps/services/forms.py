from django import forms
from .models import Service
from apps.facilities.models import Facility

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility','name','description','category','skill_type']

    def clean(self):
        cleaned_data = super().clean()
        try:
            self.instance.facility = cleaned_data.get('facility')
            self.instance.name = cleaned_data.get('name')
            self.instance.category = cleaned_data.get('category')
            self.instance.skill_type = cleaned_data.get('skill_type')
            self.instance.description = cleaned_data.get('description')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data
