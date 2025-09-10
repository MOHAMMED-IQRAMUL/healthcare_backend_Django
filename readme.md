# 🏥 Healthcare Management Backend (Django + DRF + PostgreSQL)

This project is a **Healthcare Management System** built using **Django Rest Framework (DRF)** with JWT authentication and PostgreSQL as the database.

---

## 🚀 Features

- Patient Management (CRUD)
- Doctor Management (CRUD)
- Patient-Doctor Mapping (assign doctors to patients)
- JWT Authentication (Register & Login)
- Admin Panel for superusers
- PostgreSQL / Supabase database support

---

## 🛠️ Tech Stack

- **Backend:** Django, Django Rest Framework
- **Auth:** JWT (SimpleJWT)
- **Database:** PostgreSQL / Supabase
- **Deployment Ready:** Gunicorn + PostgreSQL

---

## 📂 Project Structure

```md

healthcare\_backend/
│── manage.py
│── requirements.txt
│── README.md
│── healthcare/         # main project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
│── patients/           # Patients app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│── doctors/            # Doctors app
│── mappings/           # Patient-Doctor mapping app

````

---

## ⚙️ Setup Instructions

1. **Clone Repository**

```bash
git clone <repo-url>
cd healthcare_backend
````

1.**Create Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3.**Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4.**Setup Database**

- Configure PostgreSQL credentials in `healthcare/settings.py`
- Or connect Supabase database

5.**Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6.**Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7.**Run Server**

   ```bash
   python manage.py runserver
   ```

---

## 🔑 API Endpoints

### Authentication

- `POST /api/auth/register/` → Register new user
- `POST /api/auth/login/` → Login & get JWT token

### Patients

- `GET /api/patients/` → List all patients
- `POST /api/patients/` → Create patient
- `PUT /api/patients/{id}/` → Update patient
- `DELETE /api/patients/{id}/` → Delete patient

### Doctors

- `GET /api/doctors/` → List all doctors
- `POST /api/doctors/` → Create doctor
- `PUT /api/doctors/{id}/` → Update doctor
- `DELETE /api/doctors/{id}/` → Delete doctor

### Mappings

- `GET /api/mappings/` → List all patient-doctor mappings
- `POST /api/mappings/` → Assign patient to doctor
- `DELETE /api/mappings/{id}/` → Remove mapping

---

## 📌 Example Request

### Register a user

```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "testuser",
  "password": "securepassword123"
}
```

### Login

```http
POST /api/auth/login/
{
  "username": "testuser",
  "password": "securepassword123"
}
```

Response:

```json
{
  "refresh": "xxx...",
  "access": "yyy..."
}
```
