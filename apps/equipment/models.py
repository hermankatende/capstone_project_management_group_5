from django.db import models
from apps.facilities.models import Facility

class Equipment(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='equipment')
    name = models.CharField(max_length=140)
    capabilities = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    inventory_code = models.CharField(max_length=120, unique=False, blank=True)  # Uniqueness handled in clean()
    usage_domain = models.CharField(max_length=120, blank=True)
    support_phase = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required fields
        if not self.facility or not self.name or not self.inventory_code:
            raise ValidationError('Equipment.FacilityId, Equipment.Name, and Equipment.InventoryCode are required.')
        # Uniqueness (case-insensitive)
        qs = Equipment.objects.filter(inventory_code__iexact=self.inventory_code)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError({'inventory_code': 'Equipment.InventoryCode already exists.'})
        # UsageDomain–SupportPhase Coherence
        if (self.usage_domain or '').strip().lower() == 'electronics':
            support = (self.support_phase or '').lower()
            if not (('prototyping' in support) or ('testing' in support)):
                raise ValidationError({'support_phase': 'Electronics equipment must support Prototyping or Testing.'})

    def __str__(self):
        return f"{self.name} ({self.inventory_code})"
