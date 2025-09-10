from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient} → {self.doctor}"
