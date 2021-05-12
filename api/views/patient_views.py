from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.patient import Patient
from ..serializers import PatientSerializer, UserSerializer

# Create your views here.
class Patients(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PatientSerializer
    def get(self, request):
        """Index request"""
        patients = Patient.objects.all()
        data = PatientSerializer(patients, many=True).data
        return Response({ 'patients': data })

    def post(self, request):
        """Create request"""
        patient = PatientSerializer(data=request.data['patient'])
        if patient.is_valid():
            patient.save()
            return Response({ 'patient': patient.data }, status=status.HTTP_201_CREATED)
        return Response(patient.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PatientSerializer
    def get(self, request, pk):
        """Show request"""
        patient = get_object_or_404(Patient, pk=pk)
        data = PatientSerializer(patient).data
        return Response({ 'patient': data })

    def delete(self, request, pk):
        """Delete request"""
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        patient = get_object_or_404(Patient, pk=pk)
        data = request.data['patient']
        print('data before serialization: ', data)
        patientData = PatientSerializer(patient, data=data, partial=True)
        print('patientData serialized: ', patientData)
        if patientData.is_valid():
            patientData.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(patientData.errors, status=status.HTTP_400_BAD_REQUEST)
