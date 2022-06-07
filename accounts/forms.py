from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Doctor, Patient



class PatientSignUpForm(UserCreationForm):
    doctor = forms.ModelMultipleChoiceField(queryset=User.objects.all().filter(is_doctor=True),
        widget=forms.CheckboxSelectMultiple,
        required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    """If the block of code is successfully completed, the changes 
    are committed to the database. 
    If there is an exception, the changes are rolled back."""
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        Patient.objects.create(user=user, doctor = Doctor.objects.get(user_id=self.cleaned_data['doctor'][0])) 
        return user


class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        Doctor.objects.create(user=user)
        
        return user