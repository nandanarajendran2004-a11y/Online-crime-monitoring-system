from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CrimeReportForm
from .models import CrimeReport

def home(request):
    return render(request, 'crimeapp/home.html', {'title':'Online Crime Monitoring System'})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citizen_login')
    else:
        form = RegisterForm()
    return render(request, 'crimeapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_reports')
        else:
            return render(request, 'crimeapp/login.html', {'error':'Invalid credentials'})
    return render(request, 'crimeapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('my_reports')
    else:
        form = CrimeReportForm()
    return render(request, 'crimeapp/report.html', {'form': form})

@login_required
def my_reports(request):
    reports = CrimeReport.objects.filter(user=request.user).order_by('-date_reported')
    return render(request, 'crimeapp/myreports.html', {'reports': reports})
