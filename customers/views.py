from django.contrib import messages
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

@login_required
def customer_list(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:list')  # Redirect to refresh the page after adding
    else:
        form = CustomerForm()

    customers = Customer.objects.all()
    return render(request, 'customers/customers_list.html', {'customers': customers, 'form': form})

@login_required
def add_customer(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('customers:list')  # Redirect to the customer list after adding
        else:
            messages.error(request, 'Failed to add customer. Please correct the errors.')
    else:
        messages.error(request, 'Failed to add customer. Please correct the errors.')
        form = CustomerForm()

    return render(request, 'customers/add_customer.html', {'form': form})

@login_required
def edit_customer(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer = get_object_or_404(Customer, pk=customer_id)

        customer.name = request.POST.get('name')
        customer.contact_number = request.POST.get('contact_number')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.company_name = request.POST.get('company_name', '')

        customer.save()
        messages.success(request, 'Customer updated successfully!')
        return redirect('customers:list')

    elif request.method == 'GET':
        # Debugging or fallback for rendering an edit page directly
        customer_id = request.GET.get('customer_id')
        customer = get_object_or_404(Customer, pk=customer_id)
        form = CustomerForm(instance=customer)
        return render(request, 'customers/edit_customer.html', {'form': form, 'customer': customer})

    messages.error(request, 'Invalid request.')
    return redirect('customers:list')

@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':  # Ensure the request is POST for deletion
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('customers:list')

    messages.error(request, 'Invalid request. Customer could not be deleted.')
    return redirect('customers:list')
