# Generated by Django 5.0.6 on 2024-05-15 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=50)),
                ('sort_code', models.CharField(max_length=50)),
                ('permission', models.CharField(choices=[('MANAGER', 'Manager'), ('FINANCE', 'Finance'), ('EMPLOYEE', 'Employee')], default='EMPLOYEE', max_length=50)),
                ('date_of_joining', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateField()),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.employee')),
            ],
        ),
    ]
