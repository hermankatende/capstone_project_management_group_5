from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name','email','affiliation','specialization','cross_skill_trained','institution']

    def clean(self):
        cleaned_data = super().clean()
        try:
            self.instance.full_name = cleaned_data.get('full_name')
            self.instance.email = cleaned_data.get('email')
            self.instance.affiliation = cleaned_data.get('affiliation')
            self.instance.specialization = cleaned_data.get('specialization')
            self.instance.cross_skill_trained = cleaned_data.get('cross_skill_trained')
            self.instance.institution = cleaned_data.get('institution')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data

## ProjectParticipantForm removed
