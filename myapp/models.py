from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('office', 'Office'),
        ('driver', 'Driver'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.username} ({self.role})"
        
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

from datetime import datetime
from django.conf import settings


class Booking(models.Model):
    booking_number = models.CharField(max_length=15, unique=True, editable=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='created_bookings')
    status = models.CharField(max_length=255, default="Ongoing")

    def save(self, *args, **kwargs):
        if not self.booking_number:  # Only generate if not already set
            current_year = datetime.now().year
            last_booking = Booking.objects.filter(
                booking_number__startswith=f"{current_year}-"
            ).order_by('id').last()
            if last_booking:
                last_number = int(last_booking.booking_number.split('-')[1])
                self.booking_number = f"{current_year}-{last_number + 1:05d}"
            else:
                self.booking_number = f"{current_year}-00001"
        super().save(*args, **kwargs)
    
class Container(models.Model):
    container_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    size = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    contents = models.TextField()
    status = models.CharField(max_length=255)
    delivered_at = models.DateTimeField(null=True, blank=True)
    received_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Container {self.container_id} for Booking {self.booking}"
    
class ContainerStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    digital_signature = models.BinaryField()
    updated_at = models.DateTimeField(auto_now=True)
    received_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Status {self.status_id} for Container {self.container}"

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Unknown')
    
    # Foreign Keys to other models
    booking = models.ForeignKey('Booking', on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    container = models.ForeignKey('Container', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_booking_number(self):
        return self.booking.booking_number if self.booking else 'N/A'

    def get_customer_name(self):
        return self.customer.name if self.customer else 'N/A'

    def get_container_contents(self):
        return self.container.contents if self.container else 'N/A'


