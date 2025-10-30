from django.db import models

# Create your models here.

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
