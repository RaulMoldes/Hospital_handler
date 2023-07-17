from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=9)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    department = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length=9)
    
    def __str__(self):
        return self.name
    
class Treatment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Diagnosis(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=30)
    result = models.BooleanField()
    code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Visit(models.Model):
    id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, null=False,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=False,on_delete=models.CASCADE)
    date = models.DateField(max_length=30)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.PROTECT)
    treatment_prescribed = models.BooleanField()
    treatment = models.ForeignKey(Treatment,on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.date)