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
    
    image=models.ImageField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=25)
    age=models.PositiveIntegerField(null="True",blank="True")
    date_of_birth=models.DateField(null="True",blank="True")
    country=models.CharField(max_length=20,choices=NATIONS, default="Uganda")
    gender=models.CharField(max_length=7, choices=GENDER, default= "Female")
    student_Id =models.PositiveSmallIntegerField(null="True",blank="True")
    nationality=models.CharField(max_length=20,null="True",blank="True")
    national_Id=models.CharField(max_length=25,null="True",blank="True")
    language=models.CharField(max_length=20,null="True",blank="True")
    role_number=models.CharField(max_length=4,null="True",blank="True")
    date_of_enrolment=models.DateField(null="True",blank="True")
    medical_report=models.FileField(upload_to="images",null="True",blank="True")
    laptop_number=models.CharField(max_length=5,null="True",blank="True")
    phone_number=models.CharField(max_length=15,null="True",blank="True")
    
    def full_name(self):
       return f"{self.first_name} {self.last_name}"








    

    
        