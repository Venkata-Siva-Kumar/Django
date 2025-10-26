from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES =[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1,choices=GENDER_CHOICES)
    regNo = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.name} - {self.regNo}"
