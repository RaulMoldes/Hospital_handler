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

@login_required
def patient_data(request,patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request,"RequestHandler/patient_data.html",{"patient_data":patient})

@login_required
def doctor_data(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request,"RequestHandler/doctor_data.html",{"doctor_data":doctor})

@login_required
def visit_data(request,visit_id):
    visit = Visit.objects.get(id=visit_id)
    return render(request,"RequestHandler/visit_data.html",{"visit_data":visit})
