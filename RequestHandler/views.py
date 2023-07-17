from django.shortcuts import render
from hospital_app.forms import register_patient
from RequestHandler.models import Patient
from django import forms
# Create your views here.
def insert_patient(request):
    return render(request,"form_patient.html")

def create_patient(request):
    if request.method == "POST":
        my_forms = register_patient(request.POST)
        if my_forms.is_valid():
            info = my_forms.cleaned_data()
            ##Acceder a la info 
            patient = Patient()
            patient.id = info["id"]
            patient.name = info["name"]
            patient.surname = info["surname"]
            patient.email = info["email"]
            patient.address = info["address"]
            patient.phone_number = info["phone_number"]
            patient.save()
            print("Paciente guardado")