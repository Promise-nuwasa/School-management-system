from django.conf.urls import url
from django.urls import path
from .views import register_students,student_list,student_profile,edit_student

urlpatterns = [
    path("register",register_students,name="register_students"),
    path("list/",student_list, name ="student_list"),
    path("profile/<int:id>/",student_profile, name = "student_profile"),
    path("edit/<int:id>/",edit_student, name = "edit_student"),

     
]