from django import forms

class register_patient:
    id = forms.IntegerField(primary_key=True)
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    email = forms.EmailField(blank=True,null=True)
    phone_number = forms.CharField(max_length=9)