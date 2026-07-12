from django.urls import path
from . import views

urlpatterns = [

    # Book Appointment
    path(
        "book/",
        views.book_appointment,
        name="book_appointment"
    ),

    # My Appointments
    path(
        "my/",
        views.my_appointments,
        name="my_appointments"
    ),

]