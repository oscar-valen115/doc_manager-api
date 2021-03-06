from django.db import models
from django.contrib.auth import get_user_model
from .doctor import Doctor
 # https://docs.djangoproject.com/en/3.0/ref/models/fields/

# Create your models here.
class Patient(models.Model):
  """Patient class model """
  INACTIVE = 'inactive'
  CHECK_IN = 'check_in'
  CHECK_OUT = 'check_out'
  MALE = 'male'
  FEMALE = 'female'
  NA = ''
  status_choices = [(INACTIVE, 'inactive'), (CHECK_IN, 'check_in'), (CHECK_OUT, 'check_out')]
  gender_choices = [(MALE, 'Male'), (FEMALE, 'Female')]
  email = models.EmailField(max_length=255, unique=True, blank=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100, blank=True)
  dob = models.DateField(blank=True)
  status = models.CharField(max_length=10, choices=status_choices, default=INACTIVE)
  gender = models.CharField(max_length=10, choices=gender_choices, blank=True)
  street_address = models.CharField(max_length=200, blank=True)
  city = models.CharField(max_length=100, blank=True)
  state = models.CharField(max_length=100, blank=True)
  zip_code = models.CharField(max_length=50, blank=True)
  allergies = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  assigned_doctor = models.ForeignKey(
      Doctor,
      models.SET_NULL,
      related_name='assigned_doctor',
      null=True,
      blank=True,
  )
  def __str__(self):
    # This must return a string
    return f"The patient named '{self.first_name} {self.last_name}' date of birth is {self.dob}. They reside at {self.street_address}, {self.city}, {self.state}. They are allergic to {self.allergies}."

  def as_dict(self):
    """Returns dictionary version of Patient Model"""
    return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'dob': self.dob,
        'gender': self.gender,
        'street_address': self.street_address,
        'city': self.city,
        'state': self.state,
        'zip_code': self.zip_code,
        'status': self.status,
        'allergies': self.allergies,
        'assigned_doctor': self.assigned_doctor,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
    }
