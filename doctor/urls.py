from django.urls import path
from . import views

urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="doctor_dashboard"
    ),

    path(
        "appointments/",
        views.appointments,
        name="doctor_appointments"
    ),

    path(
        "appointments/<int:appointment_id>/approve/",
        views.approve_appointment,
        name="approve_appointment"
    ),

    path(
        "appointments/<int:appointment_id>/cancel/",
        views.cancel_appointment,
        name="cancel_appointment"
    ),

    path(
        "appointments/<int:appointment_id>/complete/",
        views.complete_appointment,
        name="complete_appointment"
    ),

]