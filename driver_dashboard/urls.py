from django.urls import path
from . import views

app_name = 'driver_dashboard'

urlpatterns = [
    path('', views.home, name='home'),
]
