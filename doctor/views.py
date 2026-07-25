from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.utils import timezone

from accounts.decorators import doctor_required

from appointments.models import Appointment


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