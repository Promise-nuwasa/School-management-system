from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=20)
    course_code=models.SmallIntegerField()
    instractor=models.CharField(max_length=25)
