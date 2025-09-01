from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    partner_organization = models.CharField(max_length=255, blank=True)
    facility_type = models.CharField(max_length=100, blank=True)
    capabilities = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
