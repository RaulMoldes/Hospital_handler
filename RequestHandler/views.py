from django.shortcuts import render

# Create your views here.
def search_patient(request):
    return render(request,"form_patient.html")

