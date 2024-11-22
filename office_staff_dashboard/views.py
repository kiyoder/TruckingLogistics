from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_office_staff(user):
    return user.profile.role == 'office_staff'

@login_required
@user_passes_test(is_office_staff)
def home(request):
    return render(request, 'office_staff_dashboard/home.html')

@login_required
@user_passes_test(is_office_staff)
def office_staff_dashboard(request):
    return render(request, 'office_staff_dashboard/office_staff_dashboard.html')

