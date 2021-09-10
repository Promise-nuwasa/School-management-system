
from django.shortcuts import render, redirect
from .forms import CoursesRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 
from .models import Courses

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form = CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("courses_list")

        else:
            return render(request, "courses_list.html")
    else:
        form= CoursesRegistrationForm()
    return render(request,"courses.html",{"form":form})

def courses_list(request):
    courses = Courses.objects.all()
    return render(request, "courses_list.html",{"courses":courses})

def edit_course(request,id):
    courses=Courses.objects.get(id=id)
    if request.method == "POST":
        form= CoursesRegistrationForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
            return redirect("courses_list", id=courses.id)
    else:
            form= CoursesRegistrationForm(instance=courses)
            return render(request,"edit_course.html",{"form":form})

            

    
    
    
    