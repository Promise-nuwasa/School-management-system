from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=20)
    course_code=models.SmallIntegerField()
    syllabus=models.CharField(max_length=50)
    course_shedule=models.DateTimeField()
    course_duration=models.DurationField()
    course_instractor=models.CharField(max_length=25)
