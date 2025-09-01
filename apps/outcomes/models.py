from django.db import models
from apps.projects.models import Project

class Outcome(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='outcomes')
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    artifact_link = models.URLField(blank=True, null=True)
    outcome_type = models.CharField(max_length=100, blank=True)
    quality_certification = models.CharField(max_length=200, blank=True, null=True)
    commercialization_status = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
