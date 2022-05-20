from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from base.decorators import patient_required, doctor_required
from django.utils.decorators import method_decorator
from accounts.models import Doctor, Patient
from .models import DailyVitals
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

"""
#@method_decorator([patient_required], name='dispatch')
class HomeView(LoginRequiredMixin, ListView):
    template_name =  'home.html'
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vitals_list', 'patients_list'] =DailyVitals.objects.filter(patient=self.request.user.patient), Patient.objects.filter(doctor=self.request.user.doctor)
        return context"""

"""
@method_decorator([doctor_required], name='dispatch')
class HomeView(LoginRequiredMixin, ListView):
    template_name =  'home.html'
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients_list = Patient.objects.filter(doctor=self.request.user.doctor)
        context['patients_list'] = patients_list
        return context"""

class HomeView(TemplateView):
    template_name =  'home.html'


class VitalCreateView(LoginRequiredMixin, CreateView):
    model = DailyVitals
    template_name =  'add_record.html'
    fields =  ['sugar_level', 'blood_pressure', 'temperature', 'weight']

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient
        return super().form_valid(form)



class PatientDetailView(TemplateView):
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vitals_list = []
        for value in DailyVitals.objects.all():
            if value.patient.user.id == self.kwargs.get('id'):
                vitals_list.append(value)

        context['vitals_list'] = vitals_list
        return context


class PatientView(ListView):
    template_name =  'patient.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vitals_list'] = DailyVitals.objects.filter(patient=self.request.user.patient)
        return context

class DoctorView(LoginRequiredMixin, ListView):
    template_name =  'doctor.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients_list = Patient.objects.filter(doctor=self.request.user.doctor)
        context['patients_list'] = patients_list
        return context