from django.db import models

# Create your models here.

class User(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]

    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    firstname=models.CharField(max_length=5,choices=COLOR_CHOICES,default="")

    
