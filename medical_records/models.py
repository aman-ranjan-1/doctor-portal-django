from django.db import models

from patient.models import Patient

from doctor.models import Doctor

from appointments.models import Appointment



class MedicalRecord(models.Model):


    patient = models.ForeignKey(

        Patient,

        on_delete=models.CASCADE,

        related_name="medical_records"

    )


    doctor = models.ForeignKey(

        Doctor,

        on_delete=models.CASCADE,

        related_name="medical_records"

    )


    appointment = models.OneToOneField(

        Appointment,

        on_delete=models.CASCADE,

        related_name="medical_record",

        null=True,

        blank=True

    )



    diagnosis = models.CharField(

        max_length=255

    )


    symptoms = models.TextField(

        blank=True

    )


    treatment = models.TextField(

        blank=True

    )


    prescription = models.TextField(

        blank=True

    )


    doctor_notes = models.TextField(

        blank=True

    )


    medical_report = models.FileField(

        upload_to="medical_reports/",

        blank=True,

        null=True

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