from django.shortcuts import render
from django.shortcuts import render
from .forms import TeacherRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 

# Create your views here.
def register_students(request):
    form= TeacherRegistrationForm()
    return render(request,"register_teacher.html",{"form":form})

