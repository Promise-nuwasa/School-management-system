from django.shortcuts import render
from django.shortcuts import render
from .forms import Courses
from django.shortcuts import render
from django.shortcuts import render 

# Create your views here.
def courses(request):
    form= Courses()
    return render(request,"courses.html",{"form":form})


