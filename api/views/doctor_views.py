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
        # Add user to request data object
        # Serialize/create mango
        doctor = DoctorSerializer(data=request.data['doctor'])
        # If the mango data is valid according to our serializer...
        if doctor.is_valid():
            # Save the created mango & send a response
            doctor.save()
            return Response({ 'doctor': doctor.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(doctor.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        mango = get_object_or_404(Mango, pk=pk)
        # Only want to show owned mangos?
        if not request.user.id == mango.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        data = MangoSerializer(mango).data
        return Response({ 'mango': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        mango = get_object_or_404(Mango, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == mango.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        mango.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['mango'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['mango'].get('owner', False):
            del request.data['mango']['owner']

        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        mango = get_object_or_404(Mango, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == mango.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Add owner to data object now that we know this user owns the resource
        request.data['mango']['owner'] = request.user.id
        # Validate updates with serializer
        data = MangoSerializer(mango, data=request.data['mango'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
