from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)  # Contact number (phone or mobile)
    email = models.EmailField(max_length=100, unique=True)  # Email must be unique
    address = models.TextField()  # Address can be long, so use TextField
    company_name = models.CharField(max_length=100, null=True, blank=True)  # Optional
    last_login = models.DateTimeField(null=True, blank=True)  # Can be updated during authentication

    def __str__(self):
        return f"{self.name} ({self.customer_id})"
