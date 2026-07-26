from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.utils import timezone

from accounts.decorators import doctor_required

from appointments.models import Appointment

from patient.models import Patient

from medical_records.models import MedicalRecord

from doctor.models import Doctor

from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncWeek



from prescriptions.models import (
    Prescription,
    PrescriptionMedicine
)
from django.shortcuts import render, redirect
from django.contrib import messages

@doctor_required
def dashboard(request):

    doctor = request.user.doctor

    today = timezone.localdate()

    appointments_today = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=today
    )

    stats = {

        "patients_today": appointments_today.values(
            "patient"
        ).distinct().count(),

        "appointments_today": appointments_today.count(),

        "completed_today": appointments_today.filter(
            status="Completed"
        ).count(),

        "pending_today": appointments_today.filter(
            status__in=[
                "Pending",
                "Confirmed"
            ]
        ).count(),

    }

    upcoming_appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date__gte=today
    ).select_related(
        "patient",
        "patient__user"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )[:5]

    recent_patients = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        "patient",
        "patient__user"
    ).order_by(
        "-appointment_date",
        "-appointment_time"
    )[:5]

    context = {

        "page_title": "Doctor Dashboard",

        "stats": stats,

        "upcoming_appointments": upcoming_appointments,

        "recent_patients": recent_patients,

        "today": today,

    }

    return render(
        request,
        "doctor/dashboard.html",
        context
    )


@doctor_required
def appointments(request):

    doctor = request.user.doctor

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        "patient",
        "patient__user"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )

    context = {

        "page_title": "Appointments",

        "appointments": appointments,

    }

    return render(
        request,
        "doctor/appointments.html",
        context
    )


@doctor_required
def approve_appointment(
    request,
    appointment_id
):

    doctor = request.user.doctor

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )

    appointment.status = "Confirmed"

    appointment.save()

    messages.success(
        request,
        "Appointment approved successfully."
    )

    return redirect(
        "doctor_appointments"
    )


@doctor_required
def cancel_appointment(
    request,
    appointment_id
):

    doctor = request.user.doctor

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )

    appointment.status = "Cancelled"

    appointment.save()

    messages.success(
        request,
        "Appointment cancelled successfully."
    )

    return redirect(
        "doctor_appointments"
    )


@doctor_required
def complete_appointment(
    request,
    appointment_id
):

    doctor = request.user.doctor

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )

    appointment.status = "Completed"

    appointment.save()

    messages.success(
        request,
        "Appointment marked as completed."
    )

    return redirect(
        "doctor_appointments"
    )


@doctor_required
def patients(request):

    doctor = request.user.doctor

    patients = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        "patient",
        "patient__user"
    ).order_by(
        "patient__user__first_name"
    )

    context = {

        "page_title": "Patients",

        "patients": patients,

    }

    return render(
        request,
        "doctor/patients.html",
        context
    )

# ==========================================
# Medical Records
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

            doctor_notes=request.POST.get("doctor_notes")

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

        "patient": patient,

    }

    return render(
        request,
        "doctor/add_medical_record.html",
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

        record.diagnosis = request.POST.get("diagnosis")

        record.symptoms = request.POST.get("symptoms")

        record.treatment = request.POST.get("treatment")

        record.prescription = request.POST.get("prescription")

        record.doctor_notes = request.POST.get("doctor_notes")

        record.save()

        messages.success(
            request,
            "Medical record updated successfully."
        )

        return redirect(
            "patient_medical_history",
            patient_id=record.patient.id
        )

    context = {

        "record": record,

    }

    return render(
        request,
        "doctor/edit_medical_record.html",
        context
    )

# ==========================================
# Prescriptions
# ==========================================

@doctor_required
def prescriptions(request):

    doctor = request.user.doctor

    today = timezone.localdate()

    patients = Patient.objects.filter(

        appointments__doctor=doctor

    ).distinct().select_related(

        "user"

    )

    prescriptions = Prescription.objects.filter(

        doctor=doctor

    ).select_related(

        "patient",

        "patient__user"

    )

    context = {

        "page_title": "Prescriptions",

        "patients": patients,

        "prescriptions": prescriptions,

        "total_prescriptions": prescriptions.count(),

        "today_prescriptions": prescriptions.filter(

            created_at__date=today

        ).count(),

        "month_prescriptions": prescriptions.filter(

            created_at__year=today.year,

            created_at__month=today.month

        ).count(),

    }

    return render(

        request,

        "doctor/prescriptions.html",

        context

    )

# ==========================================
# Prescription History
# ==========================================

@doctor_required
def prescription_history(
    request,
    patient_id
):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    prescriptions = Prescription.objects.filter(
        patient=patient
    ).order_by(
        "-created_at"
    )

    context = {

        "page_title": "Prescription History",

        "patient": patient,

        "prescriptions": prescriptions,

    }

    return render(
        request,
        "doctor/prescription_history.html",
        context
    )

# ==========================================
# Add Prescription
# ==========================================

@doctor_required
def add_prescription(
    request,
    patient_id
):

    doctor = request.user.doctor

    patient = get_object_or_404(

        Patient,

        id=patient_id

    )


    if request.method == "POST":

        diagnosis = request.POST.get(
            "diagnosis"
        )

        symptoms = request.POST.get(
            "symptoms"
        )

        medicines = request.POST.get(
            "medicines"
        )

        dosage = request.POST.get(
            "dosage"
        )

        treatment = request.POST.get(
            "treatment"
        )

        instructions = request.POST.get(
            "instructions"
        )

        follow_up_date = request.POST.get(
            "follow_up_date"
        )


        prescription = Prescription.objects.create(

        patient=patient,

        doctor=doctor,

        diagnosis=diagnosis,

        instructions=instructions,

        notes=treatment

        )

        PrescriptionMedicine.objects.create(

        prescription=prescription,

        medicine_name=medicines,

        dosage=dosage,

        frequency="",

        duration="",

        quantity=1

        )


        messages.success(

            request,

            "Prescription created successfully."

        )


        return redirect(

            "doctor_prescriptions"

        )


    context = {

        "page_title": "Add Prescription",

        "patient": patient,

    }


    return render(

        request,

        "doctor/add_prescription.html",

        context

    )
# ==========================================
# Doctor Profile
# ==========================================


@doctor_required
def profile(request):

    doctor = request.user.doctor
    user = request.user

    if request.method == "POST":

        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        doctor.phone = request.POST.get("phone")
        doctor.department = request.POST.get("department")
        doctor.specialization = request.POST.get("specialization")
        doctor.qualification = request.POST.get("qualification")
        doctor.experience = request.POST.get("experience")
        doctor.consultation_fee = request.POST.get("consultation_fee")

        doctor.available = (
            request.POST.get("available") == "True"
        )

        if request.FILES.get("profile_image"):
            doctor.profile_image = request.FILES.get(
                "profile_image"
            )


        user.save()

        doctor.save()


        messages.success(
            request,
            "Profile updated successfully!"
        )


        return redirect(
            "doctor_profile"
        )


    context = {
        "doctor":doctor,
        "user":user
    }


    return render(
        request,
        "doctor/profile.html",
        context
    )

# ==========================================
# Edit Profile
# ==========================================

@doctor_required
def edit_profile(request):

    doctor = request.user.doctor

    if request.method == "POST":

        doctor.user.first_name = request.POST.get(

            "first_name"

        )

        doctor.user.last_name = request.POST.get(

            "last_name"

        )

        doctor.user.email = request.POST.get(

            "email"

        )

        doctor.phone = request.POST.get(

            "phone"

        )

        doctor.department = request.POST.get(

            "department"

        )

        doctor.specialization = request.POST.get(

            "specialization"

        )

        doctor.qualification = request.POST.get(

            "qualification"

        )

        doctor.experience = request.POST.get(

            "experience"

        )

        doctor.consultation_fee = request.POST.get(

            "consultation_fee"

        )

        doctor.available = request.POST.get(

            "available"

        ) == "True"

        if request.FILES.get(

            "profile_image"

        ):

            doctor.profile_image = request.FILES.get(

                "profile_image"

            )

        doctor.user.save()

        doctor.save()

        messages.success(

            request,

            "Profile updated successfully."

        )

        return redirect(

            "doctor_profile"

        )

    context = {

        "page_title": "Edit Profile",

        "doctor": doctor,

        "departments": Doctor.DEPARTMENT_CHOICES,

    }

    return render(

        request,

        "doctor/edit_profile.html",

        context

    )

@doctor_required
def profile(request):

    doctor = request.user.doctor
    user = request.user

    if request.method == "POST":

        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")

        user.email = request.POST.get("email")

        doctor.phone = request.POST.get("phone")

        doctor.department = request.POST.get("department")

        doctor.specialization = request.POST.get("specialization")

        doctor.qualification = request.POST.get("qualification")

        doctor.experience = request.POST.get("experience")

        doctor.consultation_fee = request.POST.get("consultation_fee")

        doctor.available = request.POST.get("available") == "True"


        if request.FILES.get("profile_image"):
            doctor.profile_image = request.FILES.get("profile_image")


        user.save()
        doctor.save()


        messages.success(
            request,
            "Profile updated successfully!"
        )


        return redirect("doctor_profile")


    context = {

        "doctor":doctor,
        "user":user

    }


    return render(
        request,
        "doctor/profile.html",
        context
    )

@doctor_required
def schedule(request):

    doctor = request.user.doctor


    appointments = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        "patient"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )


    context = {

        "appointments":appointments

    }


    return render(
        request,
        "doctor/schedule.html",
        context
    )

@doctor_required
def report(request):

    doctor = request.user.doctor

    today = timezone.localdate()


    # ==========================
    # WEEKLY DATA
    # ==========================

    weekly_labels = []
    weekly_values = []

    for i in range(6,-1,-1):

        day = today - timedelta(days=i)

        count = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=day
        ).count()

        weekly_labels.append(
            day.strftime("%a")
        )

        weekly_values.append(
            count
        )


    # ==========================
    # MONTHLY DATA
    # ==========================

    monthly_labels = []
    monthly_values = []

    start_date = today - timedelta(days=28)

    for week in range(5):

        week_start = start_date + timedelta(
            days=week*7
        )

        week_end = week_start + timedelta(
            days=6
        )

        count = Appointment.objects.filter(
            doctor=doctor,
            appointment_date__range=[
                week_start,
                week_end
            ]
        ).count()

        monthly_labels.append(
            f"Week {week+1}"
        )

        monthly_values.append(
            count
        )


    context = {

        "weekly_labels": weekly_labels,

        "weekly_values": weekly_values,

        "monthly_labels": monthly_labels,

        "monthly_values": monthly_values,

    }


    return render(
        request,
        "doctor/report.html",
        context
    )