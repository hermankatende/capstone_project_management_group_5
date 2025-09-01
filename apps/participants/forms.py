from django import forms
from .models import Participant, ProjectParticipant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name','email','affiliation','specialization','cross_skill_trained','institution']

class ProjectParticipantForm(forms.ModelForm):
    class Meta:
        model = ProjectParticipant
        fields = ['project','participant','role_on_project','skill_role']
