from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import PatientSignUpForm, DoctorSignUpForm
from django.shortcuts import redirect
from django.http import HttpResponse


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient')


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor')


#redirects the user to the link according to the user profile
def login_success(request):
    if request.user.is_patient:
        return redirect("http://127.0.0.1:8000/patient")
    else:
        return redirect("http://127.0.0.1:8000/doctor")
        