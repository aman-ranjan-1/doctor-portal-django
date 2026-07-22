from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def patient_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if hasattr(request.user, "patient"):
            return view_func(request, *args, **kwargs)

        messages.error(request, "Patient access only.")

        return redirect("login")

    return wrapper


def doctor_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if hasattr(request.user, "doctor"):
            return view_func(request, *args, **kwargs)

        messages.error(request, "Doctor access only.")

        return redirect("login")

    return wrapper