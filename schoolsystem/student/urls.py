from django.conf.urls import url
from django.urls import path
from .views import register_students

urlpatterns = [
    path("register",register_students,name="register_students")
]