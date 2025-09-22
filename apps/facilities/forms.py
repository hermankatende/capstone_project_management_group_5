from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name','location','description','partner_organization','facility_type','capabilities']

    def clean(self):
        cleaned_data = super().clean()
        try:
            self.instance.name = cleaned_data.get('name')
            self.instance.location = cleaned_data.get('location')
            self.instance.facility_type = cleaned_data.get('facility_type')
            self.instance.capabilities = cleaned_data.get('capabilities')
            self.instance.description = cleaned_data.get('description')
            self.instance.partner_organization = cleaned_data.get('partner_organization')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data
