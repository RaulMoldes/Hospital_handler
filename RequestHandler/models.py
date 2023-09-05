from django.db import models
from LoginHandler.models import User
# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=30)
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
    hospital = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

    def __str__(self):
        return self.name


class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=False, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=False, on_delete=models.CASCADE)
    date = models.DateField(max_length=30)
    cause = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'visita'
        verbose_name_plural = 'visitas'

    def __str__(self):
        return str(self.date)
