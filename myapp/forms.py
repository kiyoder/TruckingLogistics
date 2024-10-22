from django import forms
from .models import Customer, Role, User, Booking, Container, ContainerStatus

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = '__all__'

class ContainerStatusForm(forms.ModelForm):
    class Meta:
        model = ContainerStatus
        fields = '__all__'
