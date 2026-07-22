from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):

    GENDER_CHOICES = (

        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),

    )

    BLOOD_GROUPS = (

        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),

    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient"
    )

    patient_id = models.CharField(
        max_length=20,
        unique=True
    )

    gender = models.CharField(
    max_length=10,
    choices=GENDER_CHOICES,
    blank=True
    )

    date_of_birth = models.DateField(
    null=True,
    blank=True
    )

    blood_group = models.CharField(
    max_length=5,
    choices=BLOOD_GROUPS,
    blank=True
    )

    phone = models.CharField(
    max_length=15,
    blank=True
    )

    address = models.TextField(
    blank=True
    )

    emergency_contact = models.CharField(
    max_length=15,
    blank=True
    )

    profile_image = models.ImageField(
        upload_to="patients/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.user.get_full_name()