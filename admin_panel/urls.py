from django.urls import path
from . import views

urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="admin_dashboard"
    ),

    path(
        "doctors/",
        views.doctors,
        name="admin_doctors"
    ),

    path(
        "patients/",
        views.patients,
        name="admin_patients"
    ),

    path(
        "appointments/",
        views.appointments,
        name="admin_appointments"
    ),

    path(
        "departments/",
        views.departments,
        name="admin_departments"
    ),

    path(
        "reports/",
        views.reports,
        name="admin_reports"
    ),

    path(
        "settings/",
        views.settings,
        name="admin_settings"
    ),

]