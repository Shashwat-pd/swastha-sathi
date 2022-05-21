
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from base.decorators import patient_required, doctor_required
from django.utils.decorators import method_decorator
from accounts.models import Doctor, Patient
from .models import DailyVitals, Review
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(TemplateView):
    template_name =  'home.html'

@method_decorator([patient_required], name='dispatch')
class VitalCreateView(LoginRequiredMixin, CreateView):
    model = DailyVitals
    template_name =  'add_record.html'
    fields =  ['sugar_level', 'blood_pressure', 'temperature', 'weight','monthly_report']

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
        report_list = []
        for i in DailyVitals.objects.all():
            if i.monthly_report:
                report_list.append(i.monthly_report)
        context['id'] = self.kwargs.get('id')
        context['vitals_list'] = vitals_list
        context['report_list'] = report_list
        return context

@method_decorator([patient_required], name='dispatch')
class PatientView(ListView):
    template_name =  'patient.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(patient=self.request.user.patient)
        report_list = []
        for i in DailyVitals.objects.all():
            if i.monthly_report:
                report_list.append(i.monthly_report)
        context['vitals_list'] = DailyVitals.objects.filter(patient=self.request.user.patient)
        context['reviews'] = reviews
        context['report_list'] = report_list
        return context

@method_decorator([doctor_required], name='dispatch')
class DoctorView(LoginRequiredMixin, ListView):
    template_name =  'doctor.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients_list = Patient.objects.filter(doctor=self.request.user.doctor)
        context['patients_list'] = patients_list
        return context

class ReviewCreate(CreateView):
    template_name = 'add_review.html'
    model = Review

    fields =  ['review']

    def form_valid(self, form):
        for i in Patient.objects.all():
            if i.user.id == self.kwargs.get('id'):
                form.instance.patient = Patient.objects.get(user=i.user)
        return super().form_valid(form)

    