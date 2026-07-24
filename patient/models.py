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

    MARITAL_STATUS = (
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed"),
    )

    YES_NO = (
        ("Yes", "Yes"),
        ("No", "No"),
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

    profile_image = models.ImageField(
        upload_to="patients/",
        blank=True,
        null=True
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

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS,
        blank=True
    )

    occupation = models.CharField(
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    alternate_phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    pincode = models.CharField(
        max_length=10,
        blank=True
    )

    emergency_contact_name = models.CharField(
        max_length=100,
        blank=True
    )

    emergency_contact = models.CharField(
        max_length=15,
        blank=True
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    allergies = models.TextField(
        blank=True
    )

    medical_history = models.TextField(
        blank=True
    )

    current_medications = models.TextField(
        blank=True
    )

    previous_surgeries = models.TextField(
        blank=True
    )

    insurance_provider = models.CharField(
        max_length=150,
        blank=True
    )

    insurance_number = models.CharField(
        max_length=100,
        blank=True
    )

    smoking = models.CharField(
        max_length=5,
        choices=YES_NO,
        blank=True
    )

    alcohol = models.CharField(
        max_length=5,
        choices=YES_NO,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()