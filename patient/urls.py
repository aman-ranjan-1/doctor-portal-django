from django.urls import path
from . import views

urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="patient_dashboard",
    ),
    path(
    "profile/",
    views.profile,
    name="patient_profile",
    ),
    path(
    "medical-records/",
    views.medical_records,
    name="medical_records",
    ),
]