from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from patient.forms import PatientForm
from .forms import ExtendedUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from patient.models import Patient

def home(request):
    context = {'patient':request.user}
    return render(request,'accounts/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        patient_form = PatientForm(request.POST)

        if form.is_valid() and patient_form.is_valid():
            user = form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        patient_form = PatientForm()

    context = {'form':form, 'patient_form':patient_form}
    return render(request, 'accounts/signup.html', context)

def log_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: return render(request, 'accounts/login.html', {'error':'Login is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # messages.info(request, "Logged out successfully")
    return redirect('home')
