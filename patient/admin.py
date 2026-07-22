from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (

        "patient_id",

        "user",

        "gender",

        "blood_group",

        "phone",

    )

    search_fields = (

        "patient_id",

        "user__first_name",

        "user__last_name",

        "phone",

    )

    list_filter = (

        "gender",

        "blood_group",

    )