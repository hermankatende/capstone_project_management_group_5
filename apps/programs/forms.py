from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name','description','national_alignment','focus_areas','phases']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }
