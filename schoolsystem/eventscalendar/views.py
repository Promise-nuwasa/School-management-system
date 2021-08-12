from django.shortcuts import render
from .forms import EventsRegistrationForm
from django.shortcuts import render
from django.shortcuts import render 

# Create your views here.
def eventscalendar(request):
    form= EventsRegistrationForm()
    return render(request,"events.html",{"form":form})