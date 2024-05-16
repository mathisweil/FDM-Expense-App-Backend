from django.contrib import admin

# Register your models here.

from .models import Employee, Admin

admin.site.register(Employee)
admin.site.register(Admin)