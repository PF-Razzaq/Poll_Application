from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    cnic = models.CharField(max_length=15)
    mobile_no = models.CharField(max_length=15)
    nationality = models.CharField(max_length=50)
    GENDER_CHOICES = [
        ('default','Select Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='default')
    password = models.CharField(max_length=50)
