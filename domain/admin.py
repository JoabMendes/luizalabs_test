from django.contrib import admin

# Register your models here.
from domain.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created_at', 'updated_at'
    )
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'department', 'created_at', 'updated_at'
    )
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'email']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
