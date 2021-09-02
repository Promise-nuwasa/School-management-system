from django.conf.urls import url
from django.urls import path
from .views import register_teachers,teacher_list,teacher_profile

urlpatterns = [
    path("register",register_teachers,name="register_teachers"),
    path("list/", teacher_list, name = "teacher_list"),
    path("profile/<int:id>/",teacher_profile, name = "teacher_profile"),
]