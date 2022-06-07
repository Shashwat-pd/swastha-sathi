
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from base.decorators import patient_required, doctor_required
from django.utils.decorators import method_decorator
from accounts.models import Doctor, Patient
from .models import DailyVitals, Review
from django.contrib.auth.mixins import LoginRequiredMixin

#landing page
class HomeView(TemplateView):
    template_name =  'home.html'

#form to POST data by pateint
@method_decorator([patient_required], name='dispatch')
class VitalCreateView(LoginRequiredMixin, CreateView):
    model = DailyVitals
    template_name =  'add_record.html'
    fields =  ['sugar_level', 'blood_pressure', 'temperature', 'weight','monthly_report']

    def form_valid(self, form):
        #This method is called when valid form data has been POSTed
        form.instance.patient = self.request.user.patient #user is automatically selected as the logged in user.
        return super().form_valid(form)

#Detail view of patient data to be seen by Doctor
class PatientDetailView(TemplateView):
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vitals_list = []
        #filtering queryset of vitals for passed id of the user from URL
        for value in DailyVitals.objects.all():
            if value.patient.user.id == self.kwargs.get('id'):
                vitals_list.append(value)

        #filtering queryset of reports since monthly report 
        #might be empty in some case 
        report_list = []
        for i in vitals_list:
            if i.monthly_report:
                report_list.append(i.monthly_report)

        context['id'] = self.kwargs.get('id')
        context['vitals_list'] = vitals_list
        context['report_list'] = report_list

        return context

#view for the dashboard of patient
@method_decorator([patient_required], name='dispatch')
class PatientView(ListView):
    template_name =  'patient.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.filter(patient=self.request.user.patient) #filtering reviews given by doctor to the patient
        report_list = []

        vitals_list =  DailyVitals.objects.filter(patient=self.request.user.patient)   

        for i in vitals_list:
            if i.monthly_report:
                report_list.append(i.monthly_report)

        context['vitals_list'] = vitals_list.reverse()
        context['reviews'] = reviews
        context['report_list'] = report_list
        return context

#view for the dasboard of doctor
@method_decorator([doctor_required], name='dispatch')
class DoctorView(LoginRequiredMixin, ListView):
    template_name =  'doctor.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #filtering patient queryet to the ones who signed up with logged in doctor's username
        patients_list = Patient.objects.filter(doctor=self.request.user.doctor) 
        context['patients_list'] = patients_list
        return context


#view for the form to create reviews for patient
@method_decorator([doctor_required], name='dispatch')
class ReviewCreate(CreateView):
    template_name = 'add_review.html'
    model = Review

    fields =  ['review']

    def form_valid(self, form):
        for i in Patient.objects.all():
            if i.user.id == self.kwargs.get('id'):
                form.instance.patient = Patient.objects.get(user=i.user)
        return super().form_valid(form)

    