from django.contrib import admin
from .models import Students_Info
# Register your models here.
@admin.register(Students_Info)
class SixAdmin(admin.ModelAdmin):
    list_display = ['id','roll','name', 'father_name', 'mother_name', 'mobile_number', 'date_of_birth', 'blood_group', 'result', 'address', 'class_name']
