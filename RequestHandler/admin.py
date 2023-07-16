from django.contrib import admin
from RequestHandler import models
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ["name","address","phone_number"]
    search_fields =("name",)
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name","address","phone_number"]
    search_fields =("name",)
    list_filter = ("department",)
    
class VisitAdmin(admin.ModelAdmin):
    list_display = ["patient","doctor","diagnosis","date"]
    list_filter = ("date",)
   
    
admin.site.register(models.Patient,PatientAdmin)
admin.site.register(models.Doctor,DoctorAdmin)
admin.site.register(models.Diagnosis)
admin.site.register(models.Treatment)
admin.site.register(models.Visit,VisitAdmin)