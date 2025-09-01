from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    partner_organization = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=100)
    capabilities = models.CharField(max_length=200)

    def __str__(self):
        return self.name
