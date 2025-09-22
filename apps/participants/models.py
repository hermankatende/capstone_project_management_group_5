
from django.db import models

class Participant(models.Model):
    full_name = models.CharField(max_length=140)
    email = models.EmailField(blank=True)
    affiliation = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=120, blank=True)
    cross_skill_trained = models.BooleanField(default=False)
    institution = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Required fields
        if not self.full_name or not self.email or not self.affiliation:
            raise ValidationError('Participant FullName, Participant Email, and Participant Affiliation are required.')
        # Email uniqueness (case-insensitive)
        qs = Participant.objects.filter(email__iexact=self.email)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError({'email': 'Participant Email already exists.'})
        # Specialization requirement for cross_skill_trained
        if self.cross_skill_trained and not self.specialization:
            raise ValidationError({'cross_skill_trained': 'Cross-skill flag requires Specialization.'})

    def __str__(self):
        return self.full_name
