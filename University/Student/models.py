from django.db import models
from django.utils import timezone
# Create your models here.

class Department(models.Model):
    deptID = models.CharField(max_length=10,primary_key=True)
    dName = models.CharField(max_length=30)
    location = models.CharField(max_length=100,blank=True)
    head_id = models.CharField(max_length=100,blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.deptID} - {self.dName}"
        
class Programme(models.Model):
    programmeId = models.CharField(max_length=10,primary_key=True)
    programmeName = models.CharField(max_length=30)
    offering_deptID = models.ForeignKey(Department,on_delete = models.CASCADE)
    No_of_semesters = models.PositiveSmallIntegerField(default=8)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.programmeId} - {self.programmeName}"
        

class Student(models.Model):
    registerNo = models.CharField(max_length=10,primary_key = True)
    studentName  = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    DOB = models.DateField()
    join_date = models.DateField()
    DeptID = models.ForeignKey(Department,on_delete = models.PROTECT)
    programmeID = models.ForeignKey(Programme,on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.registerNo} - {self.studentName}"
    
class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=120)
    Course_credits = models.PositiveSmallIntegerField(default=3)
    programmeID = models.ForeignKey(Programme, on_delete=models.CASCADE)
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE)
    SemesterNo = models.PositiveSmallIntegerField(default=1)

    def __str__(self): return f"{self.courseID} - {self.courseName}"
    
    
class GradeSheet(models.Model):
    registerNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    SemesterNo = models.PositiveSmallIntegerField()
    deptID = models.ForeignKey(Department, on_delete=models.PROTECT)
    ProgrammeID = models.ForeignKey(Programme, on_delete=models.PROTECT) 
    cia1 = models.PositiveSmallIntegerField(default=0)
    cia2 = models.PositiveSmallIntegerField(default=0)
    cia3 = models.PositiveSmallIntegerField(default=0)
    endsem = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f"{self.registerNo} - {self.course_id}"