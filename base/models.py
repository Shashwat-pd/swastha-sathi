from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Patient
from django.urls import reverse

# Create your models here.
class DailyVitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    blood_pressure = models.IntegerField()
    sugar_level = models.IntegerField()
    temperature = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse("patient") 


    