from django.db import models
from django.contrib.auth import get_user_model
from .doctor import Doctor
from .patient import Patient

# Create your models here.
class Appointment(models.Model):
  """Appointment class model """
  date = models.DateField(blank=True)
  time = models.TimeField(blank=True)
  # patient = models.ForeignKey()
  # doctor = models.ForeignKey()
  event_url = models.URLField(blank=True)
  attendees_email = models.EmailField(blank=True)
  reason_for_appt = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    # This must return a string
    return f"The patient named '{self.first_name} {self.last_name}' date of birth is {self.dob}. They reside at {self.street_address}, {self.city}, {self.state}. They are allergic to {self.allergies}."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'date': self.date,
        'time': self.time,
        # 'patient': self.patient,
        # 'doctor': self.doctor,
        'url': self.url,
        'reason_for_appt': self.reason_for_appt,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
    }
