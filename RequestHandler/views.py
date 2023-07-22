from django.shortcuts import render,redirect
from RequestHandler.forms import patient_form,doctor_form,visit_form
from RequestHandler.models import Patient,Doctor,Visit
from django import forms
import hospital_app.settings 
from django.core.mail import send_mail
from django.db.models import ProtectedError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
   
    if request.method == 'POST':
        form = patient_form(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('Patients')   
            
    else:
        form = patient_form(instance=patient)
        
        return render(request,"RequestHandler/patient_data.html",{"patient_data":patient,"form":form})

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = patient_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Patients')
    else:
        form = patient_form()
    return render(request, 'RequestHandler/patient_data.html', {'form': form})

@login_required
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    return redirect('Patients')

@login_required
def add_doctor(request):
    if request.method == 'POST':
        form = doctor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Doctors')
    else:
        form = doctor_form()
    return render(request, 'RequestHandler/doctor_data.html', {'form': form})

@login_required
def delete_doctor(request, doctor_id):
    
    doctor = Doctor.objects.get(id=doctor_id)
    try:
        doctor.delete()
        
    except ProtectedError as e:
        # La excepción ProtectedError se lanzará si existen otras instancias que hacen referencia a este objeto.
        # Puedes mostrar un mensaje de error personalizado o redirigir a otra página.
        messages.error(request,"No se puede eliminar el médico %s %s, ya que tiene pacientes asociados. Asigna antes otro médico de cabecera para sus pacientes"%(doctor.name,doctor.surname))
    return redirect('Doctors')   


@login_required
def add_visit(request):
    if request.method == 'POST':
        form = visit_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Visits')
    else:
        form = visit_form()
    return render(request, 'RequestHandler/visit_data.html', {'form': form})

@login_required
def delete_visit(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    visit.delete()
    return redirect('Visits')   
  
 

@login_required
def doctor_data(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = doctor_form(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
    else:
        form = doctor_form(instance=doctor)
        
    return render(request,"RequestHandler/doctor_data.html",{"doctor_data":doctor,"form":form})

@login_required
def visit_data(request,visit_id):
    visit = Visit.objects.get(id=visit_id)
    return render(request,"RequestHandler/visit_data.html",{"visit_data":visit})

