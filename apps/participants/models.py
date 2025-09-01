from django.db import models
from apps.projects.models import Project

class Participant(models.Model):
    full_name = models.CharField(max_length=140)
    email = models.EmailField(blank=True)
    affiliation = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=120, blank=True)
    cross_skill_trained = models.BooleanField(default=False)
    institution = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class ProjectParticipant(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_participants')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='assignments')
    role_on_project = models.CharField(max_length=80, blank=True)
    skill_role = models.CharField(max_length=80, blank=True)

    class Meta:
        unique_together = ('project','participant')
