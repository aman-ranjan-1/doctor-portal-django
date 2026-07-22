from django.db import models
from patient.models import Patient
from doctor.models import Doctor


class Appointment(models.Model):

    STATUS_CHOICES = [

        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),

    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField()

    symptoms = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-appointment_date", "-appointment_time"]

    def __str__(self):

        return f"{self.patient.user.get_full_name()} → Dr. {self.doctor.user.get_full_name()}"