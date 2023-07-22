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
    list_display = ["patient","doctor","procedure","date"]
    readonly_fields = ("created","updated")
    list_filter = ("date",)
    
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ["name","section","description","chapter","code"]
    readonly_fields = ("created","updated")
    list_filter = ("chapter",)
    
admin.site.register(models.Patient,PatientAdmin)
admin.site.register(models.Doctor,DoctorAdmin)
admin.site.register(models.Visit,VisitAdmin)
admin.site.register(models.Procedure,ProcedureAdmin)