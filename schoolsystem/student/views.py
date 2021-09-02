
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 
from .models import Student

# Create your views here.

def register_students(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student_list")

        else:
            return render(request, "student_list.html")
    else:
        form= StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request, "student_list.html",{"students":students})


def student_profile(request,id): 
    student=Student.objects.get(id=id)
    return render (request, "student_profile.html",{"student":student})


def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method == "POST":
        form= StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
          

            return redirect("student_profile", id=student.id)
        else:

            form= StudentRegistrationForm(instance=student)
    return redirect(request,"edit_student.html", {"form" : form})

            


    
    
    