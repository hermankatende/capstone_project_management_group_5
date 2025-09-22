
from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=120, unique=False)  # Uniqueness handled in clean()
    description = models.TextField(blank=True)
    national_alignment = models.CharField(max_length=255, blank=True)
    focus_areas = models.CharField(max_length=255, blank=True)
    phases = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required fields
        if not self.name:
            raise ValidationError({'name': 'Program.Name is required.'})
        if not self.description:
            raise ValidationError({'description': 'Program.Description is required.'})
        # Uniqueness (case-insensitive)
        qs = Program.objects.filter(name__iexact=self.name)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError({'name': 'Program.Name already exists.'})
        # National Alignment if Focus Areas are set
        recognized_tokens = ['NDPIII', 'DigitalRoadmap2023', '2028', '4IR']
        if self.focus_areas and not any(token in (self.national_alignment or '') for token in recognized_tokens):
            raise ValidationError({'national_alignment': 'Program.NationalAlignment must include at least one recognized alignment when FocusAreas are specified.'})

    def __str__(self):
        return self.name
