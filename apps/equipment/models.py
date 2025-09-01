from django.db import models
from apps.facilities.models import Facility

class Equipment(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='equipment')
    name = models.CharField(max_length=140)
    capabilities = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    inventory_code = models.CharField(max_length=120, blank=True)
    usage_domain = models.CharField(max_length=120, blank=True)
    support_phase = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.inventory_code})"
