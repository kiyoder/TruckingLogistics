from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='list'),
    path('add/', views.add_customer, name='add'),
    path('edit/', views.edit_customer, name='edit'),
    path('delete/<int:customer_id>/', views.delete_customer, name='delete'),
]
