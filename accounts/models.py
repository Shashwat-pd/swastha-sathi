from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField('doctor status', default=False)
    is_patient = models.BooleanField('patient status', default=False)

class Doctor(models.Model):
    #linking doctor model to user model 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    #linking doctor model to user model 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username



