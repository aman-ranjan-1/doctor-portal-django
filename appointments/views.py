from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Appointment
from patient.models import Patient
from doctor.models import Doctor


# ==========================================
# Book Appointment
# ==========================================

@login_required(login_url="login")
def book_appointment(request):

    try:
        patient = Patient.objects.get(user=request.user)

    except Patient.DoesNotExist:

        messages.error(request, "Patient profile not found.")

        return redirect("patient_dashboard")

    # Load all available doctors
    doctors = Doctor.objects.filter(
        available=True
    )

    if request.method == "POST":

        doctor_id = request.POST.get("doctor")

        try:

            doctor = Doctor.objects.get(
                id=doctor_id,
                available=True
            )

        except Doctor.DoesNotExist:

            messages.error(
                request,
                "Please select a valid doctor."
            )

            return redirect("book_appointment")

        Appointment.objects.create(

            patient=patient,

            doctor=doctor,

            appointment_date=request.POST.get("appointment_date"),

            appointment_time=request.POST.get("appointment_time"),

            reason=request.POST.get("reason"),

            symptoms=request.POST.get("symptoms"),

        )

        messages.success(
            request,
            "Appointment booked successfully."
        )

        return redirect("my_appointments")

    context = {

        "doctors": doctors,

    }

    return render(
        request,
        "appointments/book_appointment.html",
        context,
    )


# ==========================================
# My Appointments
# ==========================================

@login_required(login_url="login")
def my_appointments(request):

    try:

        patient = Patient.objects.get(
            user=request.user
        )

    except Patient.DoesNotExist:

        messages.error(
            request,
            "Patient profile not found."
        )

        return redirect("patient_dashboard")

    appointments = Appointment.objects.filter(
        patient=patient
    )

    context = {

        "appointments": appointments,

    }

    return render(
        request,
        "appointments/my_appointments.html",
        context,
    )