from django import forms

class register_patient(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    surname = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()