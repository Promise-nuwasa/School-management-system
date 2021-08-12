from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 
from .models import Student

# Create your views here.
def register_students(request):
    if request.method=="POST":
        form=StudentRegistrationForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form= StudentRegistrationForm()
        return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request, "student_list.html",{"student":Student})

    
    
    
    