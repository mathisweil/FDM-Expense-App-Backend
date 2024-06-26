# Generated by Django 5.0.6 on 2024-05-15 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('type', models.CharField(choices=[('MEAL', 'Meal'), ('GIFT', 'Gift'), ('OTHER', 'Other'), ('ACCOMMODATION', 'Accommodation'), ('TRAVEL', 'Travel')], max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('receipt', models.FileField(upload_to='receipts/')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('REJECTEDF', 'Rejectedf'), ('PROCESSED', 'Processed'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=50)),
                ('claimed_by', models.CharField(max_length=50)),
                ('approved_by', models.CharField(max_length=50, null=True)),
                ('approved_on', models.DateField(null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee')),
            ],
        ),
    ]
