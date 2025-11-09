from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re

# Create your models here.

def validate_multiple_of_10(value):
    if value % 10 != 0:
        raise ValidationError(f"{value} is not valid. deptID must be a multiple of 10.")
        
        
def validate_block_letter(value):
    if not re.fullmatch(r'[A-Z]', value):
        raise ValidationError(    f"{value} is invalid — blockNo must be a single uppercase letter (A–Z)." )
        
        
class Department(models.Model):
    deptID = models.IntegerField(primary_key=True,validators=[validate_multiple_of_10]  )
    deptName = models.CharField(max_length=100)
    blockNo = models.CharField(max_length=100,validators=[validate_block_letter])
    location = models.CharField(max_length=100)
        
    def __str__(self):
        return f"{self.deptName} - ({self.deptID})"
    
    
    
class Course(models.Model):
    YEAR_CHOICES = [
        ('1','I'),
        ('2','II'),
        ('3','III'),
        ('4','IV'),
    ]
    courseID = models.CharField(max_length=10,primary_key = True)
    coursename = models.CharField(max_length = 100)
    semesterNo = models.IntegerField( validators = [MinValueValidator(1),MaxValueValidator(8)],help_text="Must be between 1 and 8")
    year = models.CharField(max_length=1,choices = YEAR_CHOICES)
    
    def __str__(self):
        return f"{self.courseName} ({self.courseID})"
    
    
class Student(models.Model):
    CIA_CHOICES = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    studentID = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=100)
    CIANumber  = models.IntegerField(choices = CIA_CHOICES)
    courseID = models.ForeignKey(Course,on_delete = models.PROTECT)
    mark = models.PositiveIntegerField()
    deptID = models.ForeignKey(Department,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student_name} ({self.studentID})"
