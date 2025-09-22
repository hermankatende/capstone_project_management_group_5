from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['program','facility','title','nature_of_project','description','innovation_focus','prototype_stage','testing_requirements','commercialization_plan']
        widgets = {'description': forms.Textarea(attrs={'rows':3})}

    def clean(self):
        cleaned_data = super().clean()
        try:
            self.instance.program = cleaned_data.get('program')
            self.instance.facility = cleaned_data.get('facility')
            self.instance.title = cleaned_data.get('title')
            self.instance.nature_of_project = cleaned_data.get('nature_of_project')
            self.instance.description = cleaned_data.get('description')
            self.instance.innovation_focus = cleaned_data.get('innovation_focus')
            self.instance.prototype_stage = cleaned_data.get('prototype_stage')
            self.instance.testing_requirements = cleaned_data.get('testing_requirements')
            self.instance.commercialization_plan = cleaned_data.get('commercialization_plan')
            self.instance.clean()
        except forms.ValidationError as e:
            self.add_error(None, e)
        return cleaned_data
