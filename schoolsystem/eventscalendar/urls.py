from django.conf.urls import url
from django.urls import path
from .views import eventscalendar

urlpatterns = [
    path("register",eventscalendar,name="eventscalendar")
]