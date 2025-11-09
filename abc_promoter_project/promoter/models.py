from django.db import models

# Create your models here.

class PropertyBooking(models.Model):
    FLAT_CHOICES = [
        ('economy','Economy flat- 30 lakh rupees'),
        ('luxury','Luxury flat- 50 lakh rupees'),
        ('deluxe','Deluxe flat - 75 lakh rupees'), 
    ]
    
    HOUSE_CHOICES = [
        ('single','single house – 80 lakh'),
        ('duplex','duplex house – 1 crore'),
    ]
    
    CUSTOMER_TYPE = [
        ('flat','Flat'),
        ('HOUSE','Independent House'),
    ]
    
    name   = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email  = models.EmailField()
    
    booking_for = models.CharField(max_length = 10, choices = CUSTOMER_TYPE)
    flat_type   = models.CharField(max_length = 10, choices = FLAT_CHOICES)
    house_type  = models.CharField(max_length = 10, choices = HOUSE_CHOICES)
    
    amount  = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.name} ({self.mobile}) - {self.booking_for}"
       
    