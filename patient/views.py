from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):

    context = {
        "page_title": "Patient Dashboard"
    }

    return render(request, "patient/dashboard.html", context)