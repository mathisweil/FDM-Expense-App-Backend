# Generated by Django 5.0.6 on 2024-05-17 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_employee_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='finance_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.RESTRICT, related_name='finance', to='users.employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, related_name='manager', to='users.employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='permission',
            field=models.CharField(choices=[('FINANCE', 'Finance'), ('EMPLOYEE', 'Employee'), ('MANAGER', 'Manager')], default='EMPLOYEE', max_length=50),
        ),
    ]