from django.contrib import admin
from .models import PatientProfile, DoctorProfile

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "specialization",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "specialization",
    )