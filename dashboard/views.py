from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def role_based_dashboard(request):

    try:
        # Access the role from the user's profile
        user_role = request.user.profile.role
    except AttributeError:
        # If there is no profile or the role is not set, redirect to error page
        return redirect('error')  # You can define a custom error view

    if user_role == 'customer':
        return redirect('customer_dashboard:home')
    elif user_role == 'office_staff':
        return redirect('office_staff_dashboard:home')
    elif user_role == 'driver':
        return redirect('driver_dashboard:home')
    else:
        return redirect('error')  # Redirect to an error page if the role is invalid

