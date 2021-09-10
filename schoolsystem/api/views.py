from django.shortcuts import render
from .serializers import StudentSerializer,TeacherSerializer,CoursesSerializer,EventSerializer
from rest_framework import viewsets
from student.models import Student
from teacher.models import Teacher
from courses.models import Courses
from cal.models import Event


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class =TeacherSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset= Courses.objects.all()
    serializer_class = CoursesSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class = EventSerializer
