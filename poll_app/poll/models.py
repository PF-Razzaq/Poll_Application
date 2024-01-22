from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

class UserProfile(models.Model):
    user = ('user', models.OneToOneField(User, on_delete=models.CASCADE, default=None)),
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    cnic = models.CharField(max_length=15)
    mobile_no = models.CharField(max_length=15)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        if isinstance(self.user, tuple) and len(self.user) > 0:
            return f"Name: {self.name}\n, Email: {self.email}\n, Age: {self.age}\n, CNIC: {self.cnic}\n, Mobile: {self.mobile_no}\n, Nationality: {self.nationality}\n, Gender: {self.gender}"
        else:
            return "No associated user"
        
User = get_user_model()