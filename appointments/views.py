from django.shortcuts import render, redirect
from .models import Appointment


# -----------------------------
# Book Appointment
# -----------------------------
def book_appointment(request):

    if request.method == "POST":

        Appointment.objects.create(

            patient_name=request.POST.get("patient_name"),

            email=request.POST.get("email"),

            doctor=request.POST.get("doctor"),

            department=request.POST.get("department"),

            appointment_date=request.POST.get("appointment_date"),

            appointment_time=request.POST.get("appointment_time"),

            reason=request.POST.get("reason"),

            symptoms=request.POST.get("symptoms")

        )

        return redirect("my_appointments")

    return render(request, "appointments/book_appointment.html")


# -----------------------------
# My Appointments
# -----------------------------
def my_appointments(request):

    appointments = Appointment.objects.all().order_by("-appointment_date")

    context = {
        "appointments": appointments
    }

    return render(
        request,
        "appointments/my_appointments.html",
        context
    )