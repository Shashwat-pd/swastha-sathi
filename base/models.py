
from cgitb import text
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Patient
from django.urls import reverse

class DailyVitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=6)
    sugar_level = models.IntegerField()
    temperature = models.IntegerField()
    weight = models.IntegerField()
    monthly_report = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse("patient") 

class Review(models.Model):
    review = models.TextField(max_length=500)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse("doctor") 


