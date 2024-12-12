from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse

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
            messages.success(request, "Customer created successfully.")
            return redirect('customer_list')
        else:
            # Pass form errors to template
            return render(request, 'customers/customer_form.html', {'form': form, 'errors': form.errors})
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully.")
            return redirect('customer_list')
        else:
            # Pass form errors to template
            return render(request, 'customers/customer_form.html', {'form': form, 'errors': form.errors, 'customer': customer})
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form, 'customer': customer})
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, customer_id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

#USER
from .models import User
from .forms import UserForm

from .models import CustomUser

from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    users_by_role = {}

    for user in users:
        # Use the role directly, assuming it's a string field
        role = user.role if user.role else "Unassigned Role"
        if role not in users_by_role:
            users_by_role[role] = []
        users_by_role[role].append(user)

    return render(request, 'user/user_list.html', {'users_by_role': users_by_role})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})

from django.shortcuts import get_object_or_404
from .forms import UserForm
from .models import CustomUser

def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # Fetch the user object
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            # Save the role explicitly since it's handled in the form
            user.role = request.POST.get('role')  # Get the selected role
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user_list')  # Redirect to user list after saving
        else:
            messages.error(request, "Error updating user. Please check the form.")
    else:
        form = UserForm(instance=user)  # Pre-fill the form with the existing data
    return render(request, 'user/user_form.html', {'form': form, 'user': user})


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import CustomUser

def user_delete(request, pk):
    user = get_object_or_404(CustomUser, id=pk)  # Use 'id' instead of 'user_id'
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('user_list')  # Redirect to the user list after deletion
    return render(request, 'user/user_confirm_delete.html', {'user': user})

from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'role']  # Ensure 'role' is included
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

#BOOKINGS



from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from datetime import datetime

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Automatically set booking_number and created_by
            booking_number = form.cleaned_data['booking_number']
            booking.booking_number = booking_number
            booking.created_by = request.user
            booking.status = "Pending"
            booking.save()
            return redirect('booking_list')
    else:
        # Generate the booking number
        current_year = datetime.now().year
        last_booking = Booking.objects.filter(booking_number__startswith=str(current_year)).order_by('id').last()
        if last_booking:
            last_number = int(last_booking.booking_number.split('-')[1])
            new_number = f"{current_year}-{last_number + 1:05d}"
        else:
            new_number = f"{current_year}-00001"

        form = BookingForm(initial={'booking_number': new_number})

    return render(request, 'booking/booking_form.html', {'form': form})

# views.py
def booking_update(request, pk):
    # Fetch the existing booking object
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)  # Pass instance to update
        if form.is_valid():
            form.save()  # Save the updated instance
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)  # Pass instance for pre-filled form

    return render(request, 'booking/booking_form.html', {'form': form, 'booking': booking})


def booking_delete(request, pk):
    #booking = Booking.objects.get(booking_id=pk)
    booking = Booking.objects.get(id=pk) #updated
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})

def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = "Cancelled"
    booking.save()
    return redirect('booking_list')

def booking_confirm(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if booking.status == "Pending":
        booking.status = "Ongoing"
        booking.save()
    return redirect('booking_list')

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
            container = form.save(commit=False)
            container.status = "Pending"  # Set default status explicitly
            container.save()
            return redirect('container_list')
    else:
        form = ContainerForm()
    return render(request, 'container/container_form.html', {'form': form})


def container_update(request, pk):
    container = Container.objects.get(container_id=pk)
    if request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect('container_list')
    else:
        form = ContainerForm(instance=container)
    return render(request, 'container/container_form.html', {'form': form})

def container_delete(request, pk):
    container = Container.objects.get(container_id=pk)
    if request.method == 'POST':
        container.delete()
        return redirect('container_list')
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

from .models import Driver
from .forms import DriverForm

def driver_create(request):
    # Fetching the data to populate select fields
    bookings = Booking.objects.all()
    customers = Customer.objects.all()
    containers = Container.objects.all()

    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new driver to the database
            return redirect('/drivers/')  # Redirect directly to the list of drivers
    else:
        form = DriverForm()

    context = {
        'form': form,
        'bookings': bookings,
        'customers': customers,
        'containers': containers,
    }

    return render(request, 'driver/driver_form.html', context)

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'driver/driver_list.html', {'drivers': drivers})
def driver_update(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'driver/driver_form.html', {'form': form, 'driver': driver})

def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')  # Redirect to the driver list after deletion
    return render(request, 'driver/driver_confirm_delete.html', {'driver': driver})

def driver_form(request, pk=None):
    if pk:
        driver = get_object_or_404(Driver, pk=pk)
    else:
        driver = None

    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')  # Redirect to the driver list after saving
    else:
        form = DriverForm(instance=driver)

    return render(request, 'driver/driver_form.html', {'form': form})

#User Authentication
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            # Add validation errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        # Redirect authenticated users to the customer list page
        if request.user.is_authenticated:
            messages.info(request, f"You are already logged in as {request.user.username}.")
            return redirect('customer_list')
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)

from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_username(request):
    username = request.GET.get('value', '').strip()
    if not username:
        return JsonResponse({'valid': False, 'message': 'Username cannot be empty.'})
    if User.objects.filter(username=username).exists():
        return JsonResponse({'valid': False, 'message': 'Username is already taken.'})
    return JsonResponse({'valid': True, 'message': 'Username is available.'})

def validate_email(request):
    email = request.GET.get('value', '').strip()
    if not email:
        return JsonResponse({'valid': False, 'message': 'Email cannot be empty.'})
    if User.objects.filter(email=email).exists():
        return JsonResponse({'valid': False, 'message': 'Email is already registered.'})
    return JsonResponse({'valid': True, 'message': 'Email is available.'})


from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def logout_view(request):
    """Logs out the user and clears any remaining messages."""
    logout(request)
    for key in list(request.session.keys()):
        if key.startswith('_'):  # Preserve Django's session integrity
            continue
        del request.session[key]
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
