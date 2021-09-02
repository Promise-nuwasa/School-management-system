from django.db import models

# Create your models here.

FE = "Female"
ME = "Male"
GENDER = (
    (FE, "Female"),
    (ME, "Male")
    )
class Teacher(models.Model):
    image=models.ImageField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=25)
    email=models.EmailField(max_length=30)
    phone_number=models.CharField(max_length=14)
    age=models.PositiveIntegerField(null="True",blank="True")
    gender=models.CharField(max_length=7, choices=GENDER, default= "Female")
    nationality=models.CharField(max_length=30)
    county=models.CharField(max_length=20)
    national_id=models.CharField(max_length=40)
    languages=models.CharField(max_length=29)
    bio=models.TextField(null="True",blank="True")
    date_hired=models.DateField(null="True",blank="True")
    course=models.CharField(max_length=20)
    
    def full_name(self):
           return f"{self.first_name} {self.last_name}"



