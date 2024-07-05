from django.contrib import admin

from main_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)
