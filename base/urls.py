from django.urls import path
from .views import HomeView, VitalCreateView, DoctorView, PatientView, PatientDetailView, ReviewCreate
 

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('addRecord/', VitalCreateView.as_view(), name='create_record'),
    path('detail/<int:id>', PatientDetailView.as_view(), name='detail'),
    path('doctor', DoctorView.as_view(), name='doctor'),
    path('patient', PatientView.as_view(), name='patient'),
    path('create_review/<int:id>', ReviewCreate.as_view(), name='review_create'),
]
    

