from django import forms

class register_patient_form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    surname = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    
class contact_form(forms.Form):
    receiver = forms.EmailField()
    subject = forms.CharField()
    content = forms.CharField()