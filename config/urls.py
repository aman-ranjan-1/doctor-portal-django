from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("accounts.urls")),
    path("patient/", include("patient.urls")),
    path("appointments/", include("appointments.urls")),
    path("doctor/", include("doctor.urls")),
]
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )