from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import re
# Create your models here.


def multiple_10(value):
    if value%10 != 0:
        raise ValidationError(f"{value} is not a multiple of 10")
   
def str_check(value):
    if not re.fullmatch(r'[A-Z]',value):
        raise ValidationError(f"{value} is not a Single character of A-Z")

class Course(models.Model):
    YEAR_CHOICES =[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    ]
    courseID = models.IntegerField()
    courseName = models.CharField(max_length=50)
    semesterNo = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(8)],help_text = "Range is 1 - 8")
    year = models.CharField(max_length=1,choices = YEAR_CHOICES)
    
    def __str__(self):
        return f"{self.courseName}"
   
   

class Department(models.Model):
    deptID = models.IntegerField(validators = [multiple_10],primary_key=True)
    deptName = models.CharField(max_length = 100)
    blockNo = models.CharField(max_length=1,validators=[str_check])
    location = models.TextField()
    
    def __str__(self):
        return f"{self.deptID}"




class Student(models.Model):
    CIA_CHOICES =[
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    studentID = models.CharField(max_length=9,primary_key=True)
    student_name = models.CharField(max_length=50)
    CIANumber = models.CharField(max_length=1,choices = CIA_CHOICES)
    courseID = models.ForeignKey(Course,on_delete = models.CASCADE)
    mark = models.PositiveIntegerField()
    deptID = models.ForeignKey(Department,on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.student_name}"
    