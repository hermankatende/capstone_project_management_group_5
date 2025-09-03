from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name','email','affiliation','specialization','cross_skill_trained','institution']

## ProjectParticipantForm removed
