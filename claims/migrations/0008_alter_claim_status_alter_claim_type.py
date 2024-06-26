# Generated by Django 5.0.6 on 2024-05-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0007_remove_claim_finance_id_remove_claim_manager_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('PROCESSED', 'Processed'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending'), ('REJECTEDF', 'Rejectedf')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='type',
            field=models.CharField(choices=[('MEAL', 'Meal'), ('OTHER', 'Other'), ('GIFT', 'Gift'), ('ACCOMMODATION', 'Accommodation'), ('TRAVEL', 'Travel')], max_length=50),
        ),
    ]
