from django.db import models
from apps.programs.models import Program
from apps.facilities.models import Facility

class Project(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='projects')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=220)
    nature_of_project = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    innovation_focus = models.CharField(max_length=255, blank=True)
    prototype_stage = models.CharField(max_length=100, blank=True)
    testing_requirements = models.TextField(blank=True)
    commercialization_plan = models.TextField(blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required associations
        if not self.program or not self.facility:
            raise ValidationError('Project ProgramId and Project FacilityId are required.')
        # Name uniqueness within program (case-insensitive)
        qs = Project.objects.filter(program=self.program, title__iexact=self.title)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('A project with this name already exists in this program.')
        # Facility compatibility: testing_requirements must be in facility.capabilities
        if self.testing_requirements and self.facility and self.facility.capabilities:
            requirements = [r.strip().lower() for r in self.testing_requirements.split(',') if r.strip()]
            capabilities = self.facility.capabilities.lower()
            for req in requirements:
                if req and req not in capabilities:
                    raise ValidationError('Project requirements not compatible with facility capabilities.')

    def __str__(self):
        return self.title
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
