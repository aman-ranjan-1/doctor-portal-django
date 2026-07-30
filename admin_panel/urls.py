from django.urls import path
from . import views


urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="admin_dashboard"
    ),

    # =========================
    # DOCTORS
    # =========================

    path(
        "doctors/",
        views.doctors,
        name="admin_doctors"
    ),

    path(
        "doctors/add/",
        views.add_doctor,
        name="admin_add_doctor"
    ),

    path(
        "doctors/<int:doctor_id>/",
        views.doctor_detail,
        name="admin_doctor_detail"
    ),

    path(
        "doctors/edit/<int:doctor_id>/",
        views.edit_doctor,
        name="admin_edit_doctor"
    ),

    path(
        "doctors/delete/<int:doctor_id>/",
        views.delete_doctor,
        name="admin_delete_doctor"
    ),


    # =========================
    # PATIENTS
    # =========================

    path(
        "patients/",
        views.patients,
        name="admin_patients"
    ),
    path(
    "patients/delete/<int:patient_id>/",
    views.delete_patient,
    name="admin_delete_patient"
    ),

    # =========================
    # APPOINTMENTS
    # =========================

    path(
    "appointments/",
    views.appointments,
    name="admin_appointments"
    ),

    path(
    "appointments/<int:appointment_id>/",
    views.appointment_detail,
    name="admin_appointment_detail"
    ),

    path(
    "appointments/<int:appointment_id>/update/",
    views.update_appointment,
    name="admin_update_appointment"
    ),

    path(
    "appointments/<int:appointment_id>/delete/",
    views.delete_appointment,
    name="admin_delete_appointment"
    ),

    # =========================
    # DEPARTMENTS
    # =========================

    path(
        "departments/",
        views.departments,
        name="admin_departments"
    ),
    
    path(
    "departments/<str:department_name>/",
    views.department_detail,
    name="admin_department_detail"
    ),

    # =========================
    # REPORTS
    # =========================

    path(
        "reports/",
        views.reports,
        name="admin_reports"
    ),


    # =========================
    # SETTINGS
    # =========================

    path(
        "settings/",
        views.settings,
        name="admin_settings"
    ),

]