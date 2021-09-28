from django.db import models
from django.contrib.auth import get_user_model
# from .patient import Patient

# Create your models here.
class Doctor(models.Model):
  """Doctor class model """
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  MALE = 'male'
  FEMALE = 'female'
  gender_choices = [(MALE, 'Male'), (FEMALE, 'Female')]
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  specialty = models.CharField(max_length=100)
  with_patient = models.BooleanField(default=False)
  gender = models.CharField(max_length=10, choices=gender_choices, blank=True)
  current_patient = models.CharField(max_length=100, blank=True)
  # current_patient = models.ForeignKey(
  #   Patient,
  #   related_name='doctor_list',
  #   on_delete = models.CASCADE,
  #   blank=True,
  # )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    # This must return a string
    return f"The Doctor named '{self.first_name} {self.last_name}' specializes in {self.specialty}."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'email': self.email,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'specialty': self.specialty,
    }
