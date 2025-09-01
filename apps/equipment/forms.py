from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['facility','name','capabilities','description','inventory_code','usage_domain','support_phase']
