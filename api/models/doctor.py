from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Doctor(models.Model):
  """Doctor class model """
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  specialty = models.CharField(max_length=100)
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
