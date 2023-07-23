from django import forms
from .models import Patient,Doctor,Visit,Procedure
from LoginHandler.models import User

class patient_form(forms.ModelForm):
    
    name = forms.CharField(label="Nombre",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label="Apellido",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-mail",max_length=65,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    hospital = forms.ModelChoiceField(queryset=User.objects.all(),label="Hospital de referencia",widget = forms.Select(attrs={'class':'form-control'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(),label="Médico de cabecera",widget = forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(label="Dirección",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="Nº de teléfono",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Patient
        fields = ['name', 'surname','doctor','email', 'hospital','address','phone_number']
        

class doctor_form(forms.ModelForm):
        
    name = forms.CharField(label="Nombre",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label="Apellido",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-mail",max_length=65,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    hospital = forms.ModelChoiceField(queryset=User.objects.all(),label="Hospital de referencia",widget = forms.Select(attrs={'class':'form-control'}))
    department = forms.CharField(label="Departamento",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Dirección",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="Nº de teléfono",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Doctor
        fields = ['name', 'surname','email', 'hospital','department','address','phone_number']
        


class visit_form(forms.ModelForm):
        
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(),label="Paciente",widget=forms.Select(attrs={'class': 'form-control'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(),label="Doctor",widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(label="Fecha de la visita",input_formats=['%d/%m/%Y'],widget=forms.DateInput(attrs={'class': 'form-control','placeholder':'día/mes/año'}))
    hospital = forms.ModelChoiceField(queryset=User.objects.all(),label="Hospital de referencia",widget = forms.Select(attrs={'class':'form-control'}))
    procedure = forms.ModelChoiceField(queryset=Procedure.objects.all(),label="Motivo de la visita",widget = forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Visit
        fields = ['hospital','patient', 'doctor','date','procedure']