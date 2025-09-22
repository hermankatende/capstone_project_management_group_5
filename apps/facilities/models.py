from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    partner_organization = models.CharField(max_length=255, blank=True)
    facility_type = models.CharField(max_length=100, blank=True)
    capabilities = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required fields
        if not self.name or not self.location or not self.facility_type:
            raise ValidationError('FacilityName, FacilityLocation, and FacilityType are required.')
        # Uniqueness (case-insensitive)
        qs = Facility.objects.filter(name__iexact=self.name, location__iexact=self.location)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('A facility with this name already exists at this location.')
        # Capabilities check if Services or Equipment exist
        if self.pk:
            has_services = self.services.exists()
            has_equipment = self.equipment.exists()
            if (has_services or has_equipment) and not self.capabilities:
                raise ValidationError('Facility Capabilities must be populated when Services/Equipment exist.')

    def __str__(self):
        return self.name
