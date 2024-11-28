from django import forms
from .models import Customer, Role, User, Booking, Container, ContainerStatus, Driver

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
        model = Container
        fields = ['booking', 'size', 'weight', 'contents', 'status', 'delivered_at', 'received_by']
        widgets = {
            'booking': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'delivered_at': forms.TextInput(attrs={'class': 'form-control'}),
            'received_by': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'booking', 'customer', 'container']  # Include the necessary fields

    # If needed, you can add custom widgets or validation for the ForeignKey fields
    booking = forms.ModelChoiceField(queryset=Booking.objects.all(), required=True)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    container = forms.ModelChoiceField(queryset=Container.objects.all(), required=True)

    # If you want to customize the form further, you can add widgets or validation rules