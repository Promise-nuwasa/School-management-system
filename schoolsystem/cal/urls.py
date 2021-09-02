from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url('calendar/', views.CalendarView.as_view(), name='calendar'),
    url('list/', views.event, name='calendar_list'), 
 # here


]