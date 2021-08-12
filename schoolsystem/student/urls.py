from django.conf.urls import url
from django.urls import path
from .views import register_students
from .views import student_list

urlpatterns = [
    path("register",register_students,name="register_students"),
    path("list/",student_list,name="student_list") 
       
]