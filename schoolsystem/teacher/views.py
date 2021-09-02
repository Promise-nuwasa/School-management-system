
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 
from .models import Teacher

# Create your views here.

def register_teachers(request):
    if request.method=="POST":
        form = TeacherRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")

        else:
            return render(request, "teacher_list.html")
    else:
        form= TeacherRegistrationForm()
    return render(request,"register_teachers.html",{"form":form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html",{"teachers":teachers})

def teacher_profile(request,id): 
    teacher=Teacher.objects.get(id=id)
    return render (request, "teacher_profile.html",{"teacher":teacher})  
    
    
    