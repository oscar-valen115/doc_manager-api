# Doc Manager API

## Background

Doc Manager was built to provide doctor's offices an easy to use application to manage regular tasks at a medical office. You can create new patient records and add doctors.

Currently working on the integration with Google Calendar API to be able to schedule appointments using Google Calendar.

## Production Application

Front-End Site: (Link [here](https://oscar-valen115.github.io/doc_manager-client/))  
Front-End Repo: <https://github.com/oscar-valen115/doc_manager-client>  

Back-End Live API: <https://doc-manager-api.herokuapp.com/>  
Back-End Repo: <https://github.com/oscar-valen115/doc_manager-api>

## Technologies Used

- Python
- Django
- Django REST Framework
- Django-cors-headers
- Psycopg2
- Postgresql
- Pytz
- Gunicorn
- [Google Calendar API](https://developers.google.com/calendar)
- [Heroku](https://www.heroku.com)

## Entity Relationship Diagram  

![ERD](./staticfiles/admin/img/Capstone_Office_Assistant_ERD.jpg)

## Routes

### User

Verb | URI | Body | Headers | Status Response | Body Response
--- | --- | --- | --- | --- | ---
POST | sign-up/ | credentials | N/A | 201, Created | sign up user
POST | sign-in/ | credentials | N/A | 200, OK | sign in user
PATCH| change-pw/ | credentials | token | 204, No Content | change user password
DELETE | sign-out/ | credentials | token | 204, No Content | delete user
<!-- PATCH | update/ | credentials | token | 200, OK | update user   -->
  
### Patient

Verb | URI | Body | Headers | Status Response | Body Response
--- | --- | --- | --- | --- | ---
GET | patients/ | N/A | token | 200, OK | get all patients
POST | patients/ | patient data | token | 201, Created | create patient
PATCH| patients/{patientId}/ | patient data | token | 204, No Content | update patient
DELETE | patients/ | N/A | token | 204, No Content | delete patient

### Doctor

Verb | URI | Body | Headers | Status Response | Body Response
--- | --- | --- | --- | --- | ---
GET | doctors/ | N/A | token | 200, OK | get all doctors
POST | doctors/ | patient data | token | 201, Created | create patient
PATCH| doctors/{doctorId}/ | patient data | token | 204, No Content | update patient
DELETE | doctors/ | N/A | token | 204, No Content | delete patient  

<!--
### Calendar

Verb | URI | Body | Headers | Status Response | Body Response
--- | --- | --- | --- | --- | ---
GET | calendar/ | N/A | token | 200, OK | get all calendar events
POST | calendar/ | patient data | token | 201, Created | create calendar event
PATCH| calendar/{calendarId}/ | patient data | token | 204, No Content | update calendar event
DELETE | calendar/ | N/A | token | 204, No Content | delete calendar event  
-->