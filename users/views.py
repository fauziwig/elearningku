from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
    
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


