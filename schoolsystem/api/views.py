from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from student.models import Student


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class =StudentSerializer
