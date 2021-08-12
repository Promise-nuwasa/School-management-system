from django.shortcuts import render
from django.shortcuts import render
from .forms import TeacherRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 

# Create your views here.
def register_teachers(request):
    form= TeacherRegistrationForm()
    return render(request,"register_teacher.html",{"form":form})

