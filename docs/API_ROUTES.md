# API Routes

All responses are JSON. Use JWT in header for protected routes: `Authorization: Bearer <token>`.

## Authentication

- POST /api/auth/register/
  - body: { name, email, password }
  - 201: user created
- POST /api/auth/login/
  - body: { email, password }
  - 200: { access, refresh }

## Patients (auth required)

- POST /api/patients/
  - body: { first_name, last_name, age, gender, address }
  - 201: created patient
- GET /api/patients/
  - 200: list of patients created by current user
- GET /api/patients/`{id}`/
  - 200: patient detail
- PUT /api/patients/`{id}`/
  - body: fields to update
  - 200: updated patient
- DELETE /api/patients/`{id}`/
  - 204: deleted

## Doctors

- POST /api/doctors/ (auth required)
  - body: { first_name, last_name, specialization, years_of_experience }
  - 201: created doctor
- GET /api/doctors/
  - 200: list of doctors
- GET /api/doctors/`{id}`/
  - 200: doctor detail
- PUT /api/doctors/`{id}`/ (auth required)
  - body: fields to update
  - 200: updated doctor
- DELETE /api/doctors/`{id}`/ (auth required)
  - 204: deleted

## Patient-Doctor Mappings

- POST /api/mappings/ (auth required)
  - body: { patient_id, doctor_id }
  - 201: created mapping
- GET /api/mappings/
  - 200: list all mappings
- GET /api/mappings/`{patient_id}`/
  - 200: list doctors assigned to patient
- DELETE /api/mappings/`{id}`/ (auth required)
  - 204: deleted

## Errors

- 400: validation error `{ "detail": "..." }`
- 401: missing/invalid token
- 403: not permitted (e.g., editing someone else's patient)
- 404: not found
