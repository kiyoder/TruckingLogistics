from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('home')  # Redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
