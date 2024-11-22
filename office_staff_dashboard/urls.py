from django.urls import path
from . import views

app_name = 'office_staff_dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.office_staff_dashboard, name='office_staff_dashboard'),
]
