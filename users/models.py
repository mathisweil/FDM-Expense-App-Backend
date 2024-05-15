from django.db import models

# Create your models here.


class Employee(models.Model):
    PERMISSION = {
        ('EMPLOYEE', 'Employee'),
        ('FINANCE', 'Finance'),
        ('MANAGER', 'Manager'),
    }
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    account_number = models.CharField(max_length=50)
    sort_code = models.CharField(max_length=50)
    permission = models.CharField(max_length=50, choices=PERMISSION, default='EMPLOYEE')
    manager_id = models.ForeignKey('self', on_delete=models.RESTRICT)
    date_of_joining = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)