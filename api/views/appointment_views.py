from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token
from ..models.appointment import Appointment
from ..serializers import AppointmentSerializer

import datetime
from datetime import timedelta
import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = 'doc-manager-service-account@capstone-310616.iam.gserviceaccount.com'
SCOPES = ['https://www.googleapis.com/auth/calendar']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
  filename = 'credentials.json', scopes = SCOPES
)

# Create your views here.
class Appointments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = Appointment
    def build_service():
      service = build('calendar', 'v3', credentials=credentials)
      return service
      
    def get(self, request):
        """Index request"""
        appointments = Appointment.objects.all()
        data = Appointment(appointments, many=True).data
        return Response({ 'appointments': data })

    def post(self, request):
        """Create request"""
        appointment = Appointment(data=request.data['appointment'])
        if appointment.is_valid():
            appointment.save()
            return Response({ 'appointment': appointment.data }, status=status.HTTP_201_CREATED)
        return Response(appointment.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = Appointment
    def get(self, request, pk):
        """Show request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        data = Appointment(appointment).data
        return Response({ 'appointment': data })

    def delete(self, request, pk):
        """Delete request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        appointment = get_object_or_404(Appointment, pk=pk)
        data = request.data['appointment']
        print('data before serialization: ', data)
        appointmentData = Appointment(appointment, data=data, partial=True)
        print('appointmentData serialized: ', appointmentData)
        if appointmentData.is_valid():
            appointmentData.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(appointmentData.errors, status=status.HTTP_400_BAD_REQUEST)
