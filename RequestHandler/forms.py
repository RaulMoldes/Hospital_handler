from django import forms
from .models import Patient,Doctor

class patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['id','name', 'surname', 'email', 'hospital','address','phone_number']
        

class doctor_form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['id','name', 'surname', 'email', 'hospital','department','address','phone_number']