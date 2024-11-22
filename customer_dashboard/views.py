from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def can_access_customer_dashboard(user):
    return user.profile.role == 'customer' or user.profile.role == 'office_staff'

@login_required
@user_passes_test(can_access_customer_dashboard)
def home(request):
    return render(request, 'customer_dashboard/home.html')
