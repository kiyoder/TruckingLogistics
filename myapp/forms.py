from django import forms
from .models import Customer, Role, User, Booking, Container, ContainerStatus, Driver, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError(f"This email already exists with Customer ID: {Customer.objects.get(email=email).customer_id}")
        return email

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if Customer.objects.filter(contact_number=contact_number).exclude(pk=self.instance.pk).exists():
            raise ValidationError(f"This contact number already exists with Customer ID: {Customer.objects.get(contact_number=contact_number).customer_id}")
        return contact_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Customer.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise ValidationError(f"This name already exists with Customer ID: {Customer.objects.get(name=name).customer_id}")
        return name

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


from django import forms
from .models import Booking

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['customer', 'origin', 'destination', 'status']  # Exclude 'booking_number'
#
#     def __init__(self, *args, **kwargs):
#         super(BookingForm, self).__init__(*args, **kwargs)
#         # Add a custom read-only booking_number field if the instance exists
#         if self.instance and self.instance.pk:
#             self.fields['booking_number_display'] = forms.CharField(
#                 initial=self.instance.booking_number,
#                 label="Booking Number",
#                 required=False,
#                 widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
#             )

class BookingForm(forms.ModelForm):
    booking_number = forms.CharField(
        required=False,
        disabled=True,
        label="Booking Number",
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[
            ('Pending', 'Pending'),
            ('Ongoing', 'Ongoing'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Booking
        fields = ['customer', 'origin', 'destination', 'status']  # Exclude 'booking_number'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance or not self.instance.pk:  # New instance
            self.fields.pop('status')  # Remove status field for new bookings
        else:
            self.fields['booking_number'].initial = self.instance.booking_number


    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        if not customer:  # No customer selected
            raise forms.ValidationError("You must select an existing customer.")
        return customer

class ContainerForm(forms.ModelForm):
    booking_number = forms.ModelChoiceField(
        queryset=Booking.objects.all(),  # Fetch all bookings
        empty_label="Select a Booking",  # Optional placeholder
        label="Booking",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']