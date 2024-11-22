# myproject/urls.py
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include URLs from the accounts app
    path('', include('myapp.urls')),             # Include URLs from the myapp
    path('dashboard/', include('dashboard.urls')),
    path('customer/', include('customer_dashboard.urls')),
    path('office_staff/', include('office_staff_dashboard.urls')),
    path('driver/', include('driver_dashboard.urls')),
    path('customers/', include('customers.urls')),
]
