from django.conf.urls import url
from django.urls import path
from .views import courses

urlpatterns = [
    path("register",courses,name="courses")
]