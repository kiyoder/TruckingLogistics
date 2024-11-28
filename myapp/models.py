from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    company_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
        
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
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_number
    
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


