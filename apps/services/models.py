from django.db import models
from apps.facilities.models import Facility

class Service(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    skill_type = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required fields
        if not self.facility or not self.name or not self.category or not self.skill_type:
            raise ValidationError('Service FacilityId, Service Name, Service Category and Service SkillType are required.')
        # Scoped uniqueness (case-insensitive)
        qs = Service.objects.filter(facility=self.facility, name__iexact=self.name)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('A service with this name already exists in this facility.')

    def __str__(self):
        return f"{self.name} ({self.facility.name})"
