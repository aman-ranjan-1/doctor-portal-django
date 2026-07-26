from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from accounts.decorators import doctor_required

from appointments.models import Appointment

from prescriptions.models import Prescription

from patient.models import Patient

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