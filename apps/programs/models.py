from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    national_alignment = models.CharField(max_length=255, blank=True)
    focus_areas = models.CharField(max_length=255, blank=True)
    phases = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
