from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from patient.models import Patient
from doctor.models import Doctor


# ==========================================
# Logout
# ==========================================

def logout_page(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")


# ==========================================
# Login
# ==========================================

def login_page(request):

    if request.user.is_authenticated:

        if hasattr(request.user, "doctor"):
            return redirect("doctor_dashboard")

        if hasattr(request.user, "patient"):
            return redirect("patient_dashboard")

    if request.method == "POST":

        email = request.POST.get("email")

        password = request.POST.get("password")

        try:

            user_obj = User.objects.get(email=email)

        except User.DoesNotExist:

            messages.error(
                request,
                "No account found with this email."
            )

            return redirect("login")

        user = authenticate(

            request,

            username=user_obj.username,

            password=password

        )

        if user is None:

            messages.error(
                request,
                "Invalid email or password."
            )

            return redirect("login")

        login(request, user)

        messages.success(
            request,
            f"Welcome back, {user.first_name}!"
        )

        # ===============================
        # Role Based Redirect
        # ===============================

        if hasattr(user, "doctor"):

            return redirect("doctor_dashboard")

        elif hasattr(user, "patient"):

            return redirect("patient_dashboard")

        logout(request)

        messages.error(

            request,

            "No role has been assigned to this account."

        )

        return redirect("login")

    return render(request, "accounts/login.html")


# ==========================================
# Register
# ==========================================

def register_page(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        username = request.POST.get("username")

        email = request.POST.get("email")

        password1 = request.POST.get("password1")

        password2 = request.POST.get("password2")

        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect("register")

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password1,

            first_name=first_name,

            last_name=last_name,

        )

        # Default role = Patient

        Patient.objects.create(

            user=user,

            patient_id=f"PAT{user.id:04d}",

            gender="Male",

            date_of_birth="2000-01-01",

            blood_group="O+",

            phone="",

            address="",

            emergency_contact="",

        )

        messages.success(

            request,

            "Registration successful. Please login."

        )

        return redirect("login")

    return render(
        request,
        "accounts/register.html"
    )