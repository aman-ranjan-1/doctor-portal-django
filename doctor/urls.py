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

    path(
        "patients/",
        views.patients,
        name="doctor_patients"
    ),

    path(
        "medical-records/",
        views.medical_records,
        name="doctor_medical_records"
    ),
        path(
        "medical-records/add/<int:patient_id>/",
        views.add_medical_record,
        name="add_medical_record"
    ),

    path(
        "medical-records/history/<int:patient_id>/",
        views.patient_medical_history,
        name="patient_medical_history"
    ),

    path(
        "medical-records/detail/<int:record_id>/",
        views.medical_record_detail,
        name="medical_record_detail"
    ),

    path(
        "medical-records/edit/<int:record_id>/",
        views.edit_medical_record,
        name="edit_medical_record"
    ),
    path(
    "prescriptions/",
    views.prescriptions,
    name="doctor_prescriptions"
    ),
    path(
    "prescriptions/add/<int:patient_id>/",
    views.add_prescription,
    name="add_prescription"
    ),
    path(
    "prescriptions/history/<int:patient_id>/",
    views.prescription_history,
    name="prescription_history"
    ),
    path(
    "profile/",
    views.profile,
    name="doctor_profile"
    ),
    path(
    "profile/edit/",
    views.edit_profile,
    name="edit_profile"
    ),
    path(
    "schedule/",
    views.schedule,
    name="doctor_schedule"
    ),
    path(
    "report/",
    views.report,
    name="doctor_report"
    ),
]