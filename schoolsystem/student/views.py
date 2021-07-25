from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 

# Create your views here.
def register_students(request):
    form= StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})