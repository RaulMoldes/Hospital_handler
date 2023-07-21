from django.contrib import admin
from django.urls import path
from RequestHandler import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home,name="Home"),
    path('doctors/',views.doctors,name="Doctors"),
    path('visits/',views.visits,name="Visits"),
    path('patients/',views.patients,name="Patients"),
    path('patient_data/<int:patient_id>',views.patient_data,name="PatientData"),
    path('doctor_data/<int:doctor_id>',views.doctor_data,name="DoctorData"),
    path('visit_data/<int:visit_id>',views.visit_data,name="VisitData")
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)