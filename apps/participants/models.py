
from django.db import models

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
