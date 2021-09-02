from django.conf.urls import url
from django.urls import path
from .views import courses_list
from .views import register_courses

urlpatterns = [
    path("register" ,register_courses,name="register_courses"),
        path("list/",courses_list, name = "courses_list"),

]