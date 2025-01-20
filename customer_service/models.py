from django.db import models
from customer.models import Customer



class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('bill_issue', 'Bill Issue'),
        ('installation', 'Installation'),
        ('other', 'Other'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    details = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f'Service Request {self.id} - {self.service_type}'


class SupportTeam(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=100)  # Encrypted handling to be added

    def __str__(self):
        return self.name