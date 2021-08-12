from django.db import models

# Create your models here.

class Events(models.Model):
    Event_name=models.CharField(max_length=40)
    Event_planner=models.CharField(max_length=30)
    Event_id =models.SmallIntegerField()
    Event_date=models.DateField()
    Event_time=models.TimeField()
    Event_duration=models.DurationField()
    Event_approved_by=models.CharField(max_length=25)
    
    
