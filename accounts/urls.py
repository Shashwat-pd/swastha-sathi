from django.urls import path,include
from .views import SignUpView, PatientSignUpView, DoctorSignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='patient_signup'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='doctor_signup'),
]

