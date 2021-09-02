from django.shortcuts import render
from student.models import Student
from teacher.models import Teacher
from courses.models import Courses
from cal.models import Event



# Create your views here.
def home(request):
    students=Student.objects.count()
    teachers=Teacher.objects.count()
    courses=Courses.objects.count()
    events =Event.objects.count()
    data= {"students":students,"teachers":teachers,"courses":courses,"events":events }
    return render(request, "home.html", data)
