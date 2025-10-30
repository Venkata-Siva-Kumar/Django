from django.db import models

class WorkshopRegistration(models.Model):
    CATEGORY_CHOICES = [
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
        ('Industry', 'Industry'),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
