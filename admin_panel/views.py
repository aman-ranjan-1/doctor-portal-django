from django.shortcuts import render


def dashboard(request):
    return render(request, "admin_panel/dashboard.html")


def doctors(request):
    return render(request, "admin_panel/dashboard.html")


def patients(request):
    return render(request, "admin_panel/dashboard.html")


def appointments(request):
    return render(request, "admin_panel/dashboard.html")


def departments(request):
    return render(request, "admin_panel/dashboard.html")


def reports(request):
    return render(request, "admin_panel/dashboard.html")


def settings(request):
    return render(request, "admin_panel/dashboard.html")