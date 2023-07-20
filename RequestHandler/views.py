from django.shortcuts import render
from RequestHandler.forms import register_patient_form,contact_form
from RequestHandler.models import Patient,Doctor,Visit
from django import forms
import hospital_app.settings 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.

'''def insert_patient(request):
    return render(request,"form_patient.html")'''


def home(request):
    return render(request,"RequestHandler/home.html")


@login_required
def patients(request):
    allpatients = Patient.objects.all()
    return render(request,"RequestHandler/patients.html",{"patients":allpatients,"currentuser": request.user})

@login_required
def visits(request):
    allvisits = Visit.objects.all()
    return render(request,"RequestHandler/visits.html",{"visits":allvisits,"currentuser": request.user})

@login_required
def doctors(request):
    alldoctors = Doctor.objects.all()
    return render(request,"RequestHandler/doctors.html",{"doctors":alldoctors,"currentuser": request.user})

def contact(request):
    return render(request,"RequestHandler/contact.html")

def blog(request):
    return render(request,"RequestHandler/blog.html")