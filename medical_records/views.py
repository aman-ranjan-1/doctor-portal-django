from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from accounts.decorators import doctor_required

from patient.models import Patient

from doctor.models import Doctor

from appointments.models import Appointment

from .models import MedicalRecord



# ==========================================
# Doctor Medical Records List
# ==========================================


@doctor_required
def medical_records(request):

    doctor = request.user.doctor


    patients = Patient.objects.filter(

        appointments__doctor=doctor

    ).distinct().select_related(

        "user"

    )


    records = MedicalRecord.objects.filter(

        doctor=doctor

    )


    context = {

        "page_title": "Medical Records",

        "patients": patients,

        "records": records,

    }


    return render(

        request,

        "doctor/medical_records.html",

        context

    )





# ==========================================
# Add Medical Record
# ==========================================


@doctor_required
def add_medical_record(request, patient_id):

    doctor = request.user.doctor


    patient = get_object_or_404(

        Patient,

        id=patient_id

    )


    if request.method == "POST":


        MedicalRecord.objects.create(

            patient=patient,

            doctor=doctor,

            diagnosis=request.POST.get("diagnosis"),

            symptoms=request.POST.get("symptoms"),

            treatment=request.POST.get("treatment"),

            prescription=request.POST.get("prescription"),

            doctor_notes=request.POST.get("doctor_notes"),

            medical_report=request.FILES.get("medical_report")

        )


        messages.success(

            request,

            "Medical record added successfully."

        )


        return redirect(

            "patient_medical_history",

            patient_id=patient.id

        )



    context = {

        "page_title": "Add Medical Record",

        "patient": patient,

    }


    return render(

        request,

        "doctor/edit_medical_record.html",

        context

    )





# ==========================================
# Patient Medical History
# ==========================================


@doctor_required
def patient_medical_history(request, patient_id):

    doctor = request.user.doctor


    patient = get_object_or_404(

        Patient,

        id=patient_id

    )


    records = MedicalRecord.objects.filter(

        patient=patient,

        doctor=doctor

    )


    context = {

        "page_title": "Patient Medical History",

        "patient": patient,

        "records": records,

    }


    return render(

        request,

        "doctor/patient_medical_history.html",

        context

    )





# ==========================================
# Medical Record Detail
# ==========================================


@doctor_required
def medical_record_detail(request, record_id):

    doctor = request.user.doctor


    record = get_object_or_404(

        MedicalRecord,

        id=record_id,

        doctor=doctor

    )


    context = {

        "page_title": "Medical Record Detail",

        "record": record,

    }


    return render(

        request,

        "doctor/medical_record_detail.html",

        context

    )





# ==========================================
# Edit Medical Record
# ==========================================


@doctor_required
def edit_medical_record(request, record_id):

    doctor = request.user.doctor


    record = get_object_or_404(

        MedicalRecord,

        id=record_id,

        doctor=doctor

    )


    if request.method == "POST":


        record.diagnosis = request.POST.get(
            "diagnosis"
        )

        record.symptoms = request.POST.get(
            "symptoms"
        )

        record.treatment = request.POST.get(
            "treatment"
        )

        record.prescription = request.POST.get(
            "prescription"
        )

        record.doctor_notes = request.POST.get(
            "doctor_notes"
        )


        if request.FILES.get(
            "medical_report"
        ):

            record.medical_report = request.FILES.get(
                "medical_report"
            )


        record.save()


        messages.success(

            request,

            "Medical record updated successfully."

        )


        return redirect(

            "medical_record_detail",

            record_id=record.id

        )



    context = {

        "page_title": "Edit Medical Record",

        "record": record,

    }


    return render(

        request,

        "doctor/edit_medical_record.html",

        context

    )