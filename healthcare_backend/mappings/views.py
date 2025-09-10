from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()
