from django.urls import path

from . import views


urlpatterns = [

    path(
        "add/<int:patient_id>/",
        views.add_medical_record,
        name="add_medical_record"
    ),


    path(
        "history/<int:patient_id>/",
        views.patient_medical_history,
        name="patient_medical_history"
    ),


    path(
        "detail/<int:record_id>/",
        views.medical_record_detail,
        name="medical_record_detail"
    ),


    path(
        "edit/<int:record_id>/",
        views.edit_medical_record,
        name="edit_medical_record"
    ),

]