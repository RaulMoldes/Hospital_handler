from django.shortcuts import render
from RequestHandler.forms import register_patient_form,contact_form
from RequestHandler.models import Patient
from django import forms
import hospital_app.settings 
from django.core.mail import send_mail
# Create your views here.

'''def insert_patient(request):
    return render(request,"form_patient.html")'''


def home(request):
    return render(request,"RequestHandler/home.html")

def account(request):
    return render(request,"RequestHandler/account.html")

def messages(request):
    return render(request,"RequestHandler/messages.html")

def patients(request):
    return render(request,"RequestHandler/patients.html")

def contact(request):
    return render(request,"RequestHandler/contact.html")

def blog(request):
    return render(request,"RequestHandler/blog.html")