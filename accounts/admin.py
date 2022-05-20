from django.contrib import admin
from .models import (Patient, Doctor, User)

# Register your models here.
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Doctor)
