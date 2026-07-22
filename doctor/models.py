from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    DEPARTMENT_CHOICES = [

        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Dermatology", "Dermatology"),
        ("Pediatrics", "Pediatrics"),
        ("Gynecology", "Gynecology"),
        ("General Medicine", "General Medicine"),
        ("ENT", "ENT"),
        ("Ophthalmology", "Ophthalmology"),
        ("Psychiatry", "Psychiatry"),

    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor"
    )

    doctor_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES
    )

    specialization = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=150
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in Years"
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    phone = models.CharField(
        max_length=15
    )

    profile_image = models.ImageField(
        upload_to="doctors/",
        blank=True,
        null=True
    )

    available = models.BooleanField(
        default=True
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Dr. {self.user.get_full_name()}"