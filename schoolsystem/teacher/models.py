from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=25)
    Email=models.EmailField(max_length=30)
    Phone_number=models.CharField(max_length=14)
    course=models.CharField(max_length=20)

