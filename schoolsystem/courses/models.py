from django.db import models

# Create your models here.
class Courses(models.Model):
    Course_name=models.CharField(max_length=20)
    Course_code=models.SmallIntegerField()
    Syllabus=models.CharField(max_length=50)
    Course_shedule=models.DateTimeField()
    Course_duration=models.DurationField()
    Course_Instractor=models.CharField(max_length=25)
