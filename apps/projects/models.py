from django.db import models
from programs.models import Program
from facilities.models import Facility

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
