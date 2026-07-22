from django.shortcuts import render
from accounts.decorators import doctor_required

@doctor_required
def dashboard(request):

    context = {

        "page_title": "Doctor Dashboard",

    }

    return render(
        request,
        "doctor/dashboard.html",
        context
    )