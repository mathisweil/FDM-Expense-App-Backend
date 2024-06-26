# Generated by Django 5.0.6 on 2024-05-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_alter_claim_status_alter_claim_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claim',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('REJECTEDF', 'Rejectedf'), ('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('REJECTED', 'Rejected'), ('PROCESSED', 'Processed')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='type',
            field=models.CharField(choices=[('ACCOMMODATION', 'Accommodation'), ('MEAL', 'Meal'), ('OTHER', 'Other'), ('TRAVEL', 'Travel'), ('GIFT', 'Gift')], max_length=50),
        ),
        migrations.AlterModelTable(
            name='claim',
            table='claims',
        ),
    ]
