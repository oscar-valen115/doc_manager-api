from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.doctor import Doctor
from ..serializers import DoctorSerializer, UserSerializer

# Create your views here.
class Doctors(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = DoctorSerializer
    def get(self, request):
        """Index request"""
        # Get all the mangos:
        # mangos = Mango.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        doctors = Doctor.objects.all()
        # Run the data through the serializer
        data = DoctorSerializer(doctors, many=True).data
        return Response({ 'doctors': data })

    def post(self, request):
        """Create request"""
        data = request.data['doctor']
        doctor = DoctorSerializer(data=data)
        # If the mango data is valid according to our serializer...
        if doctor.is_valid():
            # Save the created mango & send a response
            doctor.save()
            return Response({ 'doctor': doctor.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        print(doctor.errors)
        return Response(doctor.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        doctor = get_object_or_404(Doctor, pk=pk)
        # Run the data through the serializer so it's formatted
        data = DoctorSerializer(doctor).data
        return Response({ 'doctor': data })

    def delete(self, request, pk):
        """Delete request"""
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Doctor
        # get_object_or_404 returns a object representation of our Mango
        doctor = get_object_or_404(Doctor, pk=pk)
        # Validate updates with serializer
        data = DoctorSerializer(doctor, data=request.data['doctor'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
