# Doc Manager API

## Background
Doc Manager was built to provide doctor's offices an easy to use application to manage regular tasks at a medical office. You can create new patient records, add doctors, and schedule appointments through google calendar API calls all with an easy to use interface.

## Production Application
Front-End Site: (Link [here](https://oscar-valen115.github.io/doc_manager-client/))  
Front-End Repo: https://github.com/oscar-valen115/doc_manager-client  

Back-End Live API: https://doc-manager-api.herokuapp.com/  
Back-End Repo: https://github.com/oscar-valen115/doc_manager-api

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
POST | sign-in/ | credentials | N/A | 201, Created | sign in user
PATCH| change-pw/ | credentials | token | 204, No Content | change user password
DELETE | sign-out/ | credentials | token | 204, No Content | delete user
<!-- PATCH| update/ | credentials | token | 200, OK | update user   -->
  
  
### Patient

Verb | URI | Body | Headers | Status Response | Body Response
--- | --- | --- | --- | --- | ---
GET | patients/ | N/A | token | 200, OK | get all patients
POST | patients/ | patient data | token | 201, Created | create patient
PATCH| patients/{patientId}/ | patient data | token | 204, No Content | update patient
DELETE | patients/ | N/A | token | 204, No Content | delete patient