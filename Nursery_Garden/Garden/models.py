from django.db import models

# Create your models here.
class Plant_Details(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    benefit = models.TextField()
    
    def __str__(self):
        return self.name
        