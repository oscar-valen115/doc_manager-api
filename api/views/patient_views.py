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
        # Get all the mangos:
        # mangos = Mango.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        patients = Patient.objects.all()
        # Run the data through the serializer
        data = PatientSerializer(patients, many=True).data
        return Response({ 'patients': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        # Serialize/create patient
        patient = PatientSerializer(data=request.data['patient'])
        if patient.is_valid():
            # Save the created patient & send a response
            patient.save()
            return Response({ 'patient': patient.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(patient.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PatientSerializer
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        patient = get_object_or_404(Patient, pk=pk)
        # Run the data through the serializer so it's formatted
        data = PatientSerializer(patient).data
        return Response({ 'patient': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate patient to delete
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        print('request data: ', request.data)
        patient = get_object_or_404(Patient, pk=pk)
        data = request.data['patient']
        # data = request.data
        print('data info: ', data)
        patientData = PatientSerializer(patient, data=data, partial=True)
        print('patientData serialized: ', patientData)
        if patientData.is_valid():
            # Save & send a 204 no content
            patientData.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        # print(patientData.errors)
        return Response(patientData.errors, status=status.HTTP_400_BAD_REQUEST)
