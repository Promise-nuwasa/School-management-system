from django.conf.urls import url
from django.urls import path
from .views import courses_list
from .views import register_courses, edit_course

urlpatterns = [
    path("register" ,register_courses,name="register_courses"),
        path("list/",courses_list, name = "courses_list"),
            path("edit/<int:id>/",edit_course, name = "edit_course"),


]