from django.db import models

# Create your models here.
class Department(models.Model):
    deptNo = models.PositiveIntegerField(primary_key=True)
    dName  = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.dName

class Employee(models.Model):
    empno = models.PositiveIntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    sex   = models.CharField(max_length=1,choices=[('M','Male'),('F','Female'),])
    join_date = models.DateField()
    salary = models.FloatField()
    deptNo = models.ForeignKey(Department,on_delete = models.CASCADE)

    def __str__(self):
        return self.ename
