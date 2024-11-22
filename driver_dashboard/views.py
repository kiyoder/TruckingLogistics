from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def can_access_driver_dashboard(user):
    return user.profile.role == 'driver' or user.profile.role == 'office_staff'

@login_required
@user_passes_test(can_access_driver_dashboard)
def home(request):
    return render(request, 'driver_dashboard/home.html')
