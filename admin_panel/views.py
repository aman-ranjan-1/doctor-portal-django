from datetime import timedelta
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count

from doctor.models import Doctor
from patient.models import Patient
from appointments.models import Appointment

from django.core.paginator import Paginator
from doctor.models import Doctor
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from prescriptions.models import Prescription

from datetime import timedelta
from django.utils import timezone

from django.shortcuts import get_object_or_404, redirect


def dashboard(request):

    today = timezone.localdate()

    total_doctors = Doctor.objects.count()

    total_patients = Patient.objects.count()

    today_appointments = Appointment.objects.filter(
        appointment_date=today
    ).count()

    completed_appointments = Appointment.objects.filter(
        status="Completed"
    ).count()

    pending_appointments = Appointment.objects.filter(
        status="Pending"
    ).count()

    cancelled_appointments = Appointment.objects.filter(
        status="Cancelled"
    ).count()

    recent_appointments = Appointment.objects.select_related(
        "patient__user",
        "doctor__user"
    ).order_by(
        "-appointment_date",
        "-appointment_time"
    )[:5]

    chart_labels = []

    chart_values = []

    for i in range(6, -1, -1):

        day = today - timedelta(days=i)

        chart_labels.append(
            day.strftime("%a")
        )

        chart_values.append(

            Appointment.objects.filter(
                appointment_date=day
            ).count()

        )

    context = {

        "total_doctors": total_doctors,

        "total_patients": total_patients,

        "today_appointments": today_appointments,

        "completed_appointments": completed_appointments,

        "pending_appointments": pending_appointments,

        "cancelled_appointments": cancelled_appointments,

        "recent_appointments": recent_appointments,

        "chart_labels": chart_labels,

        "chart_values": chart_values,

        "page_title": "Dashboard",

    }

    return render(
        request,
        "admin_panel/dashboard.html",
        context
    )


from django.shortcuts import render
from doctor.models import Doctor


def doctors(request):

    search = request.GET.get(
        "search",
        ""
    )

    department = request.GET.get(
        "department",
        ""
    )

    doctors = Doctor.objects.select_related(
        "user"
    ).all()

    if search:

        doctors = doctors.filter(
            user__first_name__icontains=search
        ) | Doctor.objects.filter(
            user__last_name__icontains=search
        ) | Doctor.objects.filter(
            doctor_id__icontains=search
        )

    if department:

        doctors = doctors.filter(
            department=department
        )

    paginator = Paginator(
        doctors.order_by("doctor_id"),
        10
    )

    page_number = request.GET.get(
        "page"
    )

    page_obj = paginator.get_page(
        page_number
    )

    context = {

        "page_obj": page_obj,

        "search": search,

        "selected_department": department,

        "departments": Doctor.DEPARTMENT_CHOICES,

        "total_doctors": Doctor.objects.count(),

        "active_doctors": Doctor.objects.filter(
            available=True
        ).count(),

        "inactive_doctors": Doctor.objects.filter(
            available=False
        ).count(),

        "total_departments": Doctor.objects.values(
            "department"
        ).distinct().count(),

    }

    return render(
        request,
        "admin_panel/doctors.html",
        context
    )

@login_required 
def patients(request):

    search = request.GET.get(
        "search",
        ""
    )

    patients = Patient.objects.select_related(
        "user"
    ).prefetch_related(
        "appointments__doctor__user"
    )


    if search:

        patients = patients.filter(
            patient_id__icontains=search
        ) | patients.filter(
            user__first_name__icontains=search
        ) | patients.filter(
            user__last_name__icontains=search
        )


    paginator = Paginator(
        patients.order_by("patient_id"),
        10
    )


    page_obj = paginator.get_page(
        request.GET.get("page")
    )


    context = {

        "page_obj": page_obj,

        "search": search,

        "total_patients": Patient.objects.count(),

    }


    return render(
        request,
        "admin_panel/patients.html",
        context
    )

def delete_patient(request, patient_id):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )


    if request.method == "POST":

        patient.user.delete()

        messages.success(
            request,
            "Patient deleted successfully."
        )


    return redirect(
        "admin_patients"
    )

@login_required
def appointments(request):

    search = request.GET.get(
        "search",
        ""
    )

    status = request.GET.get(
        "status",
        ""
    )


    appointments = Appointment.objects.select_related(
        "patient__user",
        "doctor__user"
    ).all()



    if search:

        appointments = appointments.filter(

            patient__user__first_name__icontains=search

        ) | appointments.filter(

            doctor__user__first_name__icontains=search

        )



    if status:

        appointments = appointments.filter(
            status=status
        )



    paginator = Paginator(
        appointments.order_by(
            "-appointment_date",
            "-appointment_time"
        ),
        10
    )


    page_number = request.GET.get(
        "page"
    )


    page_obj = paginator.get_page(
        page_number
    )



    context = {


        "page_obj": page_obj,


        "search": search,


        "selected_status": status,


        "statuses": Appointment.STATUS_CHOICES,


        "total_appointments": Appointment.objects.count(),


        "pending_count": Appointment.objects.filter(
        status="Pending"
        ).count(),

        "confirmed_count": Appointment.objects.filter(
            status="Confirmed"
        ).count(),

        "completed_count": Appointment.objects.filter(
            status="Completed"
        ).count(),

        "cancelled_count": Appointment.objects.filter(
            status="Cancelled"
        ).count(),


    }



    return render(

        request,

        "admin_panel/appointments.html",

        context

    )
def update_appointment_status(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    if request.method == "POST":

        status = request.POST.get(
            "status"
        )

        appointment.status = status

        appointment.save()


        messages.success(
            request,
            "Appointment status updated successfully."
        )


    return redirect(
        "admin_appointments"
    )




def delete_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    if request.method == "POST":

        appointment.delete()


        messages.success(
            request,
            "Appointment deleted successfully."
        )


    return redirect(
        "admin_appointments"
    )

def appointment_detail(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    context = {

        "appointment": appointment

    }


    return render(
        request,
        "admin_panel/appointment_detail.html",
        context
    )
def update_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    if request.method == "POST":

        status = request.POST.get(
            "status"
        )

        appointment.status = status

        appointment.save()


        messages.success(
            request,
            "Appointment status updated."
        )


    return redirect(
        "admin_appointment_detail",
        appointment.id
    )

def delete_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    if request.method == "POST":

        appointment.delete()


        messages.success(
            request,
            "Appointment deleted successfully."
        )


    return redirect(
        "admin_appointments"
    )

@login_required
def departments(request):

    departments = []

    for value, label in Doctor.DEPARTMENT_CHOICES:

        doctor_count = Doctor.objects.filter(
            department=value
        ).count()


        available_count = Doctor.objects.filter(
            department=value,
            available=True
        ).count()


        departments.append({

            "name": label,

            "value": value,

            "doctor_count": doctor_count,

            "available_count": available_count,

        })


    context = {


        "departments": departments,


        "total_departments": len(
            departments
        ),


        "total_doctors": Doctor.objects.count()


    }


    return render(

        request,

        "admin_panel/departments.html",

        context

    )

def department_detail(request, department_name):

    doctors = Doctor.objects.filter(
        department=department_name
    ).select_related(
        "user"
    )


    department_label = dict(
        Doctor.DEPARTMENT_CHOICES
    ).get(
        department_name
    )


    context = {

        "department_name": department_label,

        "doctors": doctors,

        "total_doctors": doctors.count(),

    }


    return render(
        request,
        "admin_panel/department_detail.html",
        context
    )

@login_required
def reports(request):

    total_doctors = Doctor.objects.count()

    total_patients = Patient.objects.count()

    total_appointments = Appointment.objects.count()


    completed_appointments = Appointment.objects.filter(
        status="Completed"
    ).count()


    pending_appointments = Appointment.objects.filter(
        status="Pending"
    ).count()


    cancelled_appointments = Appointment.objects.filter(
        status="Cancelled"
    ).count()



    department_data = []

    for value, label in Doctor.DEPARTMENT_CHOICES:

        count = Doctor.objects.filter(
            department=value
        ).count()


        department_data.append({

            "department": label,

            "count": count

        })




    appointment_labels = []

    appointment_values = []


    today = timezone.localdate()


    for i in range(6,-1,-1):

        day = today - timedelta(days=i)


        appointment_labels.append(
            day.strftime("%a")
        )


        appointment_values.append(

            Appointment.objects.filter(
                appointment_date=day
            ).count()

        )




    context = {


        "total_doctors": total_doctors,


        "total_patients": total_patients,


        "total_appointments": total_appointments,


        "completed_appointments": completed_appointments,


        "pending_appointments": pending_appointments,


        "cancelled_appointments": cancelled_appointments,


        "department_data": department_data,


        "appointment_labels": appointment_labels,


        "appointment_values": appointment_values,


    }


    return render(

        request,

        "admin_panel/reports.html",

        context

    )

@login_required
def settings(request):

    context = {

        "admin_name": request.user.get_full_name(),

        "admin_email": request.user.email,

    }


    return render(

        request,

        "admin_panel/settings.html",

        context

    )

def generate_doctor_id():

    last_doctor = Doctor.objects.order_by(
        "-id"
    ).first()

    if last_doctor:

        last_number = int(
            last_doctor.doctor_id.replace(
                "DOC",
                ""
            )
        )

        return f"DOC{last_number + 1:04d}"

    return "DOC1001"

def add_doctor(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        email = request.POST.get("email")

        password = request.POST.get("password")

        department = request.POST.get("department")

        specialization = request.POST.get("specialization")

        qualification = request.POST.get("qualification")

        experience = request.POST.get("experience")

        consultation_fee = request.POST.get("consultation_fee")

        phone = request.POST.get("phone")

        available = request.POST.get(
            "available"
        ) == "True"

        profile_image = request.FILES.get(
            "profile_image"
        )

        if User.objects.filter(
            username=email
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect(
                "admin_add_doctor"
            )

        user = User.objects.create_user(

            username=email,

            email=email,

            password=password,

            first_name=first_name,

            last_name=last_name

        )

        Doctor.objects.create(

            user=user,

            doctor_id=generate_doctor_id(),

            department=department,

            specialization=specialization,

            qualification=qualification,

            experience=experience,

            consultation_fee=consultation_fee,

            phone=phone,

            profile_image=profile_image,

            available=available

        )

        messages.success(

            request,

            "Doctor added successfully."

        )

        return redirect(
            "admin_doctors"
        )

    context = {

        "departments": Doctor.DEPARTMENT_CHOICES

    }

    return render(

        request,

        "admin_panel/add_doctor.html",

        context

    )

def doctor_detail(request, doctor_id):

    doctor = Doctor.objects.select_related(
        "user"
    ).get(
        id=doctor_id
    )

    appointments = Appointment.objects.filter(
        doctor=doctor
    )

    prescriptions = Prescription.objects.filter(
        doctor=doctor
    )

    managed_patients = Patient.objects.filter(
    appointments__doctor=doctor
    ).distinct().count()

    today = timezone.localdate()

    activity_days = []

    for i in range(34, -1, -1):

        day = today - timedelta(days=i)

        has_activity = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=day
        ).exists()

        activity_days.append({

            "date": day,

            "active": has_activity

        })

    context = {

        "doctor": doctor,

        "appointments_count": appointments.count(),

        "completed_count": appointments.filter(
            status="Completed"
        ).count(),

        "pending_count": appointments.filter(
            status="Pending"
        ).count(),

        "managed_patients": managed_patients,

        "prescriptions_count": prescriptions.count(),

        "recent_appointments": appointments.order_by(
            "-appointment_date",
            "-appointment_time"
        )[:5],

        "recent_prescriptions": prescriptions.order_by(
            "-created_at"
        )[:5],

        "activity_days": activity_days,

    }

    return render(

        request,

        "admin_panel/doctor_detail.html",

        context

    )

def edit_doctor(request, doctor_id):

    doctor = get_object_or_404(

        Doctor.objects.select_related("user"),

        id=doctor_id

    )

    if request.method == "POST":

        doctor.user.first_name = request.POST.get(
            "first_name"
        )

        doctor.user.last_name = request.POST.get(
            "last_name"
        )

        doctor.user.email = request.POST.get(
            "email"
        )

        doctor.user.username = request.POST.get(
            "email"
        )

        doctor.department = request.POST.get(
            "department"
        )

        doctor.specialization = request.POST.get(
            "specialization"
        )

        doctor.qualification = request.POST.get(
            "qualification"
        )

        doctor.experience = request.POST.get(
            "experience"
        )

        doctor.consultation_fee = request.POST.get(
            "consultation_fee"
        )

        doctor.phone = request.POST.get(
            "phone"
        )

        doctor.available = (

            request.POST.get(

                "available"

            ) == "True"

        )

        if request.FILES.get(

            "profile_image"

        ):

            doctor.profile_image = request.FILES.get(

                "profile_image"

            )

        doctor.user.save()

        doctor.save()

        messages.success(

            request,

            "Doctor updated successfully."

        )

        return redirect(

            "admin_doctor_detail",

            doctor.id

        )

    context = {

        "doctor": doctor,

        "departments": Doctor.DEPARTMENT_CHOICES,

    }

    return render(

        request,

        "admin_panel/edit_doctor.html",

        context

    )

def delete_doctor(request, doctor_id):

    doctor = get_object_or_404(

        Doctor.objects.select_related(
            "user"
        ),

        id=doctor_id

    )

    if request.method == "POST":

        doctor.user.delete()

        messages.success(

            request,

            "Doctor deleted successfully."

        )

        return redirect(

            "admin_doctors"

        )

    context = {

        "doctor": doctor

    }

    return render(

        request,

        "admin_panel/delete_doctor.html",

        context

    )