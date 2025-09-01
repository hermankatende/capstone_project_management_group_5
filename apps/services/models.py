from django.db import models
from apps.facilities.models import Facility

class Service(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    skill_type = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.facility.name})"
