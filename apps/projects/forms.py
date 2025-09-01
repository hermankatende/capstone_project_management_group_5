from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['program','facility','title','nature_of_project','description','innovation_focus','prototype_stage','testing_requirements','commercialization_plan']
        widgets = {'description': forms.Textarea(attrs={'rows':3})}
