# Generated by Django 5.0.6 on 2024-05-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_employee_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='permission',
            field=models.CharField(choices=[('FINANCE', 'Finance'), ('EMPLOYEE', 'Employee'), ('MANAGER', 'Manager')], default='EMPLOYEE', max_length=50),
        ),
    ]
