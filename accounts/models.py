from django.db import models
from django.contrib.auth.models import User


class PatientProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient - {self.user.username}"


class DoctorProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    specialization = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doctor - {self.user.username}"