# Generated by Django 5.0.6 on 2024-05-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_alter_claim_options_alter_claim_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('REJECTEDF', 'Rejectedf'), ('APPROVED', 'Approved'), ('PROCESSED', 'Processed'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='type',
            field=models.CharField(choices=[('GIFT', 'Gift'), ('ACCOMMODATION', 'Accommodation'), ('TRAVEL', 'Travel'), ('MEAL', 'Meal'), ('OTHER', 'Other')], max_length=50),
        ),
    ]