from django.db import models

# Create your models here.
class Student(models.Model):

    UG = "Uganda"
    KE = "Kenya"
    RW = "Rwanda"
    SS = "South Sudan"
    SN = "South"
    NATIONS = (
        (UG, "Uganda"),
        (KE, "Kenya"),
        (RW, "Rwanda"),
        (SS, "South Sudan"),
        (SN, "Sudan")

    )
    FE = "Female"
    ME = "Male"
    GENDER = (
        (FE, "Female"),
        (ME, "Male")
    )
    
    profile=models.ImageField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=25)
    age=models.PositiveIntegerField()
    date_of_birth=models.DateField()
    country=models.CharField(max_length=20,choices=NATIONS, default="Uganda")
    gender=models.CharField(max_length=7, choices=GENDER, default= "Female")
    student_Id =models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=20)
    national_Id=models.CharField(max_length=25)
    language=models.CharField(max_length=20)
    role_number=models.CharField(max_length=4)
    date_of_enrolment=models.DateField()
    medical_report=models.FileField()
    laptop_number=models.CharField(max_length=5)
    phone_number=models.CharField(max_length=14)
    







    

    
        