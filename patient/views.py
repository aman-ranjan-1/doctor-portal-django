from django.shortcuts import render
from accounts.decorators import patient_required
from appointments.models import Appointment

@patient_required
def dashboard(request):

    appointments = Appointment.objects.filter(
        user=request.user
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

    return render(
        request,
        "patient/dashboard.html",
        context
    )