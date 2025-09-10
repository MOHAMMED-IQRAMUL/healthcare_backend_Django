from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # creator
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
