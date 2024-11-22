from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.role_based_dashboard, name='role_based_dashboard'),
    # path('office_staff/home/', views.office_staff_home, name='office_staff_home')
]
