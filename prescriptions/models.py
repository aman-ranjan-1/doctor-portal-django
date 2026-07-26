from django.db import models

from patient.models import Patient

from doctor.models import Doctor

from appointments.models import Appointment


class Prescription(models.Model):

    patient = models.ForeignKey(

        Patient,

        on_delete=models.CASCADE,

        related_name="prescriptions"

    )

    doctor = models.ForeignKey(

        Doctor,

        on_delete=models.CASCADE,

        related_name="prescriptions"

    )

    appointment = models.OneToOneField(

        Appointment,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="prescription"

    )

    diagnosis = models.CharField(

        max_length=255

    )

    instructions = models.TextField(

        blank=True

    )

    notes = models.TextField(

        blank=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "-created_at"

        ]

    def __str__(self):

        return f"{self.patient.user.get_full_name()} - {self.diagnosis}"


class PrescriptionMedicine(models.Model):

    prescription = models.ForeignKey(

        Prescription,

        on_delete=models.CASCADE,

        related_name="medicines"

    )

    medicine_name = models.CharField(

        max_length=150

    )

    dosage = models.CharField(

        max_length=100

    )

    frequency = models.CharField(

        max_length=100

    )

    duration = models.CharField(

        max_length=100

    )

    quantity = models.PositiveIntegerField(

        default=1

    )

    def __str__(self):

        return self.medicine_name