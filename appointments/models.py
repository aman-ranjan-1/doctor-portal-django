from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="appointments"
)
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]

    patient_name = models.CharField(max_length=100)

    email = models.EmailField()

    doctor = models.CharField(max_length=100)

    department = models.CharField(max_length=100)

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField()

    symptoms = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor}"