from django.db import models
from LoginHandler.models import User
# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctors",default='doctors/doc1.png')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    department = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctores'
    
    def __str__(self):
        return self.name
    

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,null = True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="patients",default='patients/pat1.png')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
    
    def __str__(self):
        return self.name
    
class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    chapter = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'procedimiento'
        verbose_name_plural = 'procedimientos'
    
    def __str__(self):
        return self.name
    
class Parameter(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=65)
    units = models.CharField(max_length=30)
    code = models.CharField(max_length = 35)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'parámetro'
        verbose_name_plural = 'parámetros'
    
    def __str__(self):
        return self.name
    
class Treatment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'tratamiento'
        verbose_name_plural = 'tratamientos'
    
    def __str__(self):
        return self.name
    
class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'diagnóstico'
        verbose_name_plural = 'diagnósticos'
    
    def __str__(self):
        return self.name

class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    hp_uuid = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=False,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=False,on_delete=models.CASCADE)
    date = models.DateField(max_length=30)
    diagnosis = models.ForeignKey(Diagnosis,null = True, on_delete=models.PROTECT)
    treatment = models.ForeignKey(Treatment,null = True,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'visita'
        verbose_name_plural = 'vistas'
        
    def __str__(self):
        return str(self.date)
