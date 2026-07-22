from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "doctor_id",
        "user",
        "department",
        "specialization",
        "experience",
        "consultation_fee",
        "available",
    )

    search_fields = (
        "doctor_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "department",
        "specialization",
    )

    list_filter = (
        "department",
        "available",
    )

    ordering = (
        "department",
        "user__first_name",
    )