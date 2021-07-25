from django.conf.urls import url
from django.urls import path
from .views import register_teachers

urlpatterns = [
    path("register",register_teachers,name="register_teachers")
]