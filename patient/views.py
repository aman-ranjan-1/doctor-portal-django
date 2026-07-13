from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment


@login_required(login_url='login')
def dashboard(request):

    appointments = Appointment.objects.filter(user=request.user)

    # Dashboard Statistics
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

    # Upcoming Appointments
    upcoming_appointments = appointments.order_by(
        "appointment_date"
    )[:5]

    context = {
        "page_title": "Patient Dashboard",
        "total_appointments": total_appointments,
        "confirmed_appointments": confirmed_appointments,
        "pending_appointments": pending_appointments,
        "cancelled_appointments": cancelled_appointments,
        "upcoming_appointments": upcoming_appointments,
    }

    return render(request, "patient/dashboard.html", context)