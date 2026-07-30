# CityCare - Hospital Management System

A full-stack Hospital Management System built with **Django** that streamlines interactions between patients, doctors, and administrators. The application provides role-based authentication, appointment scheduling, medical record management, prescription tracking, and a centralized administrative dashboard.

**Live Demo:** https://doctor-portal-django.onrender.com/

**Admin Login:** https://doctor-portal-django.onrender.com/accounts/admin-login/

### Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| Administrator | admin@citycare.com | Admin@123 |

> **Note:** The hosted application uses a demo administrator account for evaluation purposes.

---

# Features

## Public Website

- Responsive landing page
- About section
- Services section
- Doctors showcase
- Contact section
- Authentication pages

## Authentication

- Patient registration
- Patient login
- Doctor login
- Administrator login
- Role-based authentication
- Protected dashboards
- Session management

## Patient Module

- Patient dashboard
- Profile management
- Appointment booking
- Appointment history
- Medical records
- Prescription history

## Doctor Module

- Doctor dashboard
- Appointment management
- Patient information
- Prescription management
- Availability management
- Profile management

## Appointment Management

- Appointment scheduling
- Appointment confirmation
- Appointment cancellation
- Appointment completion
- Appointment status tracking

## Medical Records

- Medical history
- Current medications
- Prescription records
- Patient details
- Doctor notes

## Administrator Panel

- Dashboard analytics
- Doctor management
- Patient management
- Appointment management
- Reports
- System settings

---

# Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 4.6
- Font Awesome

## Backend

- Python
- Django

## Database

- SQLite (Development)

## Deployment

- Render

---

# Project Structure

```text
doctor-portal/
├── accounts/
├── admin_panel/
├── appointments/
├── config/
├── doctor/
├── home/
├── medical_records/
├── patient/
├── prescriptions/
├── static/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/doctor-portal.git
cd doctor-portal
```

## Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# Screenshots

- Home Page
- Patient Dashboard
- Doctor Dashboard
- Administrator Dashboard
- Appointment Management
- Reports

---

# Future Enhancements

- Email notifications
- Payment gateway integration
- Online video consultation
- Doctor scheduling calendar
- PDF prescription generation
- Advanced analytics
- REST API
- Docker deployment
- PostgreSQL production database

---

# License

This project is developed for educational, learning, and internship purposes.

---

# Developer

**Aman Ranjan**
