from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField

class GoogleCredentialsModel(models.Model):
  """ Handles Google API Credentials """
  id = models.ForeignKey
