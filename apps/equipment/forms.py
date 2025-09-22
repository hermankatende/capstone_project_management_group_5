from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['facility','name','capabilities','description','inventory_code','usage_domain','support_phase']

    def clean(self):
        cleaned_data = super().clean()
        # Call model clean for all business rules
        try:
            self.instance.facility = cleaned_data.get('facility')
            self.instance.name = cleaned_data.get('name')
            self.instance.inventory_code = cleaned_data.get('inventory_code')
            self.instance.usage_domain = cleaned_data.get('usage_domain')
            self.instance.support_phase = cleaned_data.get('support_phase')
            self.instance.capabilities = cleaned_data.get('capabilities')
            self.instance.description = cleaned_data.get('description')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data


