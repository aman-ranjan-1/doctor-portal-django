from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PatientProfile
from doctor.models import Doctor
# =====================================================
# Logout
# =====================================================

def logout_page(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")

# =====================================================
# Login
# =====================================================

def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(
                    request,
                    f"Welcome back, {user.first_name or user.username}!"
                )

                if Doctor.objects.filter(user=user).exists():

                    return redirect("doctor_dashboard")

                elif PatientProfile.objects.filter(user=user).exists():

                    return redirect("patient_dashboard")

                logout(request)

                messages.error(
                    request,
                    "No account role has been assigned. Please contact the administrator."
                )

                return redirect("login")

            else:

                messages.error(
                    request,
                    "Invalid password."
                )

        except User.DoesNotExist:

            messages.error(
                request,
                "No account found with this email."
            )

        return redirect("login")

    return render(
        request,
        "accounts/login.html"
    )
# =====================================================
# Register
# =====================================================

def register_page(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Password Match

        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")

        # Username Exists

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        # Email Exists

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already registered."
            )

            return redirect("register")

        # Create User

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1,
        )

        messages.success(
            request,
            "Account created successfully. Please login."
        )

        return redirect("login")

    return render(
        request,
        "accounts/register.html"
    )