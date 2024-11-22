from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role_id', 'created_at', 'last_login')  # Use fields from the User model
    list_filter = ('role_id',)  # Add valid filter fields
    search_fields = ('email', 'username')  # Use valid searchable fields
