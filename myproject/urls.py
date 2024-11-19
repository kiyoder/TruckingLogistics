# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include URLs from the accounts app
    path('', include('myapp.urls')),             # Include URLs from the myapp
]
