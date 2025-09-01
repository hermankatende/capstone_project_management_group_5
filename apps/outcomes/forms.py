from django import forms
from .models import Outcome

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = '__all__'
