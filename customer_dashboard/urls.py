from django.urls import path
from . import views

app_name = 'customer_dashboard'

urlpatterns = [
    path('', views.home, name='home'),
]
