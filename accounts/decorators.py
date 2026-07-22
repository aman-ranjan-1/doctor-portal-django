from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages

from patient.models import Patient
from doctor.models import Doctor


# ==========================================
# Patient Required
# ==========================================

def patient_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            messages.warning(
                request,
                "Please login first."
            )

            return redirect("login")

        if not Patient.objects.filter(user=request.user).exists():

            messages.error(
                request,
                "Access denied."
            )

            return redirect("login")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================
# Doctor Required
# ==========================================

def doctor_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            messages.warning(
                request,
                "Please login first."
            )

            return redirect("login")

        if not Doctor.objects.filter(user=request.user).exists():

            messages.error(
                request,
                "Access denied."
            )

            return redirect("login")

        return view_func(request, *args, **kwargs)

    return wrapper