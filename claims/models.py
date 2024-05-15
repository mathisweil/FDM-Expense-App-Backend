from django.db import models

# Create your models here.


class Claim(models.Model):
    TYPE = {
        ('TRAVEL', 'Travel'),
        ('MEAL', 'Meal'),
        ('ACCOMMODATION', 'Accommodation'),
        ('GIFT', 'Gift'),
        ('OTHER', 'Other'),
    }
    STATUS = {
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('PROCESSED', 'Processed'),
        ('REJECTED', 'Rejected'),
        ('REJECTEDF', 'Rejectedf'),
    }
    claim_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('users.Employee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    type = models.CharField(max_length=50, choices=TYPE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    receipt = models.FileField(upload_to='receipts/')
    status = models.CharField(max_length=50, choices=STATUS, default='PENDING')
    claimed_by = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=50, null=True)
    approved_on = models.DateField(null=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title