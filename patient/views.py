from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import patient_required
from patient.models import Patient
from appointments.models import Appointment


@patient_required
def dashboard(request):

    patient = Patient.objects.get(user=request.user)

    appointments = Appointment.objects.filter(
        patient=patient
    )

    context = {

        "page_title": "Patient Dashboard",

        "patient": patient,

        "total_appointments": appointments.count(),

        "confirmed_appointments": appointments.filter(
            status="Confirmed"
        ).count(),

        "pending_appointments": appointments.filter(
            status="Pending"
        ).count(),

        "cancelled_appointments": appointments.filter(
            status="Cancelled"
        ).count(),

        "upcoming_appointments": appointments.order_by(
            "appointment_date",
            "appointment_time"
        )[:5],

    }

    return render(
        request,
        "patient/dashboard.html",
        context
    )


@patient_required
def profile(request):

    patient = Patient.objects.get(
        user=request.user
    )

    if request.method == "POST":

        # -------------------------
        # Django User Fields
        # -------------------------

        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")
        request.user.save()

        # -------------------------
        # Patient Fields
        # -------------------------

        patient.gender = request.POST.get("gender")
        patient.date_of_birth = request.POST.get("date_of_birth") or None
        patient.blood_group = request.POST.get("blood_group")
        patient.marital_status = request.POST.get("marital_status")
        patient.occupation = request.POST.get("occupation")

        patient.phone = request.POST.get("phone")
        patient.alternate_phone = request.POST.get("alternate_phone")

        patient.address = request.POST.get("address")
        patient.city = request.POST.get("city")
        patient.state = request.POST.get("state")
        patient.pincode = request.POST.get("pincode")

        patient.emergency_contact_name = request.POST.get(
            "emergency_contact_name"
        )

        patient.emergency_contact = request.POST.get(
            "emergency_contact"
        )

        patient.height = request.POST.get("height") or None
        patient.weight = request.POST.get("weight") or None

        patient.allergies = request.POST.get("allergies")
        patient.medical_history = request.POST.get("medical_history")
        patient.current_medications = request.POST.get("current_medications")
        patient.previous_surgeries = request.POST.get("previous_surgeries")

        patient.insurance_provider = request.POST.get(
            "insurance_provider"
        )

        patient.insurance_number = request.POST.get(
            "insurance_number"
        )

        patient.smoking = request.POST.get("smoking")
        patient.alcohol = request.POST.get("alcohol")

        # -------------------------
        # Profile Image
        # -------------------------

        if request.FILES.get("profile_image"):

            patient.profile_image = request.FILES.get(
                "profile_image"
            )

        patient.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("patient_profile")

    context = {

        "patient": patient,

    }

    return render(
        request,
        "patient/profile.html",
        context
    )


@patient_required
def medical_records(request):

    patient = Patient.objects.get(
        user=request.user
    )

    records = []

    context = {

        "patient": patient,

        "medical_records": records,

    }

    return render(
        request,
        "patient/medical_records.html",
        context
    )