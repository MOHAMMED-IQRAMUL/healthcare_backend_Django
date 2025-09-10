from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # creator
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    # gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, null=True, blank=True)

    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
