from django.shortcuts import render
# from student.models import Student
# from teacher.models import Teacher
# from courses.models import Courses
# from cal.models import Event



# Create your views here.
def home(request):
    return render(request, "home.html")