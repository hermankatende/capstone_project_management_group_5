from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    national_alignment = models.CharField(max_length=200)
    focus_areas = models.CharField(max_length=200)
    phases = models.CharField(max_length=200)

    def __str__(self):
        return self.name