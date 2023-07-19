from django.contrib import admin
from RequestHandler import models
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ["name","address","phone_number"]
    readonly_fields = ("created","updated")
    search_fields =("name",)
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name","address","phone_number"]
    readonly_fields = ("created","updated")
    search_fields =("name",)
    list_filter = ("department",)
    
class VisitAdmin(admin.ModelAdmin):
    list_display = ["patient","doctor","diagnosis","date"]
    readonly_fields = ("created","updated")
    list_filter = ("date",)

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ["name","description","section","code","start_date","end_date"]
    readonly_fields = ("created","updated")
    list_filter = ("section",)
    
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["name","description","section","code"]
    readonly_fields = ("created","updated")
    list_filter = ("section",)
    
    
admin.site.register(models.Patient,PatientAdmin)
admin.site.register(models.Doctor,DoctorAdmin)
admin.site.register(models.Diagnosis,DiagnosisAdmin)
admin.site.register(models.Treatment,TreatmentAdmin)
admin.site.register(models.Visit,VisitAdmin)