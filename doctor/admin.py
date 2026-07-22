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

        "available",

    )

    search_fields = (

        "doctor_id",

        "user__first_name",

        "user__last_name",

        "department",

        "specialization",

    )

    list_filter = (

        "department",

        "available",

    )