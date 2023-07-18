from django.contrib import admin
from django.urls import path
from RequestHandler import views

urlpatterns = [
    
    path('',views.home,name="Home"),
    path('services/',views.services,name="Services"),
    path('account/',views.account,name="Account"),
    path('messages/',views.messages,name="Messages"),
    path('patients/',views.patients,name="Patients"),
    path('contact/',views.contact,name="Contact"),
]
