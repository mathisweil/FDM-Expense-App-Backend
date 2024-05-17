# Generated by Django 5.0.6 on 2024-05-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='permission',
            field=models.CharField(choices=[('MANAGER', 'Manager'), ('FINANCE', 'Finance'), ('EMPLOYEE', 'Employee')], default='EMPLOYEE', max_length=50),
        ),
    ]
