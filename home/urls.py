from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("doctors/", views.doctors, name="doctors"),
    path(
    "medical-blog/",
    views.medical_blog,
    name="medical_blog"
    ),
]