from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name','description','national_alignment','focus_areas','phases']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Call model clean for all business rules
        try:
            self.instance.name = cleaned_data.get('name')
            self.instance.description = cleaned_data.get('description')
            self.instance.national_alignment = cleaned_data.get('national_alignment')
            self.instance.focus_areas = cleaned_data.get('focus_areas')
            self.instance.phases = cleaned_data.get('phases')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data
