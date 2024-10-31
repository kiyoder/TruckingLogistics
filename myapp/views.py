from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'role/role_form.html')
#ROLE
from .models import Role
from .forms import RoleForm

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role/role_list.html', {'roles': roles})

def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role/role_list')
    else:
        form = RoleForm()
    return render(request, 'role/role_form.html', {'form': form})

def role_update(request, pk):
    role = Role.objects.get(role_id=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role/role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role_form.html', {'form': form})

def role_delete(request, pk):
    role = Role.objects.get(role_id=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role/role_list')
    return render(request, 'role/role_confirm_delete.html', {'role': role})

#CUSTOMER
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

from django.shortcuts import redirect

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})


def customer_update(request, pk):
    # Fetch the existing customer instance by primary key
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        # Bind the form to the existing customer instance
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()  # Updates the existing customer
            return redirect('customer_list')  # Redirect to the customer list after saving
    else:
        # Initialize the form with the existing data for editing
        form = CustomerForm(instance=customer)
    
    return render(request, 'customers/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, customer_id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

#USER
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})

def user_update(request, pk):
    user = User.objects.get(user_id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user/user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, user_id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user/user_confirm_delete.html', {'user': user})

#BOOKINGS

from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking/booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_update(request, pk):
    booking = Booking.objects.get(booking_id=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking/booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_delete(request, pk):
    booking = Booking.objects.get(booking_id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking/booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})


#CONTAINER
from .models import Container
from .forms import ContainerForm

def container_list(request):
    containers = Container.objects.all()
    return render(request, 'container/container_list.html', {'containers': containers})

def container_create(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('container/container_list')
    else:
        form = ContainerForm()
    return render(request, 'container/container_form.html', {'form': form})

def container_update(request, pk):
    container = Container.objects.get(container_id=pk)
    if request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect('container/container_list')
    else:
        form = ContainerForm(instance=container)
    return render(request, 'container/container_form.html', {'form': form})

def container_delete(request, pk):
    container = Container.objects.get(container_id=pk)
    if request.method == 'POST':
        container.delete()
        return redirect('container/container_list')
    return render(request, 'container/container_confirm_delete.html', {'container': container})

#CONTAINER STATUS
from .models import ContainerStatus
from .forms import ContainerStatusForm

def container_status_list(request):
    statuses = ContainerStatus.objects.all()
    return render(request, 'container_status/container_status_list.html', {'statuses': statuses})

def container_status_create(request):
    if request.method == 'POST':
        form = ContainerStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('container_status/container_status_list')
    else:
        form = ContainerStatusForm()
    return render(request, 'container_status/container_status_form.html', {'form': form})

def container_status_update(request, pk):
    status = ContainerStatus.objects.get(status_id=pk)
    if request.method == 'POST':
        form = ContainerStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('container_status/container_status_list')
    else:
        form = ContainerStatusForm(instance=status)
    return render(request, 'container_status/container_status_form.html', {'form': form})

def container_status_delete(request, pk):
    status = ContainerStatus.objects.get(status_id=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('container_status/container_status_list')
    return render(request, 'container_status/container_status_confirm_delete.html', {'status': status})

