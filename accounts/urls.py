from django.urls import path,include
from .views import SignUpView, PatientSignUpView, DoctorSignUpView
from base.views import DoctorView, PatientView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='patient_signup'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='doctor_signup'),
    path('doctor', DoctorView.as_view(), name='doctor'),
    path('patient', PatientView.as_view(), name='patient'),
]

