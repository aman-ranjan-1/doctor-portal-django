from django.shortcuts import render
from accounts.decorators import patient_required
from patient.models import Patient
from appointments.models import Appointment


@patient_required
def dashboard(request):

    patient = Patient.objects.get(
        user=request.user
    )

    appointments = Appointment.objects.filter(
        patient=patient
    )

    total_appointments = appointments.count()

    confirmed_appointments = appointments.filter(
        status="Confirmed"
    ).count()

    pending_appointments = appointments.filter(
        status="Pending"
    ).count()

    cancelled_appointments = appointments.filter(
        status="Cancelled"
    ).count()

    upcoming_appointments = appointments.order_by(
        "appointment_date",
        "appointment_time"
    )[:5]

    context = {

        "page_title": "Patient Dashboard",

        "patient": patient,

        "total_appointments": total_appointments,

        "confirmed_appointments": confirmed_appointments,

        "pending_appointments": pending_appointments,

        "cancelled_appointments": cancelled_appointments,

        "upcoming_appointments": upcoming_appointments,

    }

    return render(
        request,
        "patient/dashboard.html",
        context
    )

@patient_required
def profile(request):

    patient = Patient.objects.get(user=request.user)

    context = {

        "patient": patient,

    }

    return render(
        request,
        "patient/profile.html",
        context,
    )

@patient_required
def medical_records(request):

    records = []

    context = {

        "records": records,

    }

    return render(
        request,
        "patient/medical_records.html",
        context,
    )