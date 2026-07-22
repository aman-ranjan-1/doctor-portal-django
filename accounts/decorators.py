from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import PatientProfile
from doctor.models import Doctor


def patient_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            return redirect("login")

        if PatientProfile.objects.filter(user=request.user).exists():

            return view_func(request, *args, **kwargs)

        messages.error(request, "You are not authorized to access this page.")

        return redirect("login")

    return wrapper


def doctor_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            return redirect("login")

        if Doctor.objects.filter(user=request.user).exists():

            return view_func(request, *args, **kwargs)

        messages.error(request, "You are not authorized to access this page.")

        return redirect("login")

    return wrapper