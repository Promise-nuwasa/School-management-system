from django.db import models



# Create your models here.

FE = "Female"
ME = "Male"
GENDER = (
    (FE, "Female"),
    (ME, "Male")
    )
class Teacher(models.Model):
    profile=models.ImageField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=25)
    Email=models.EmailField(max_length=30)
    Phone_number=models.CharField(max_length=14)
    Age=models.PositiveIntegerField()
    Gender=models.CharField(max_length=7, choices=GENDER, default= "Female")
    Nationality=models.CharField(max_length=30)
    county=models.CharField(max_length=20)
    National_id=models.CharField(max_length=40)
    Languages=models.CharField(max_length=29)
    Bio=models.TextField()
    Date_hired=models.DateField()
    course=models.CharField(max_length=20)
    


