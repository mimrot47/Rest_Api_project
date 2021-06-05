from django.contrib import admin
from .models import Employee

# Register your modelslist_display = 


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','esal','ename','eaddr']
