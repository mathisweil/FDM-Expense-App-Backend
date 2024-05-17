# Generated by Django 5.0.6 on 2024-05-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0008_alter_claim_status_alter_claim_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('REJECTEDF', 'Rejectedf'), ('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('PROCESSED', 'Processed')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='type',
            field=models.CharField(choices=[('ACCOMMODATION', 'Accommodation'), ('TRAVEL', 'Travel'), ('OTHER', 'Other'), ('MEAL', 'Meal'), ('GIFT', 'Gift')], max_length=50),
        ),
    ]