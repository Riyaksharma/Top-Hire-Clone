from django.shortcuts import render, redirect
from .models import User, JobRole, UserRole
from django.contrib import messages
from .forms import CreateUser, UserInterestedRolesForm

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def dashboard(request):
    return render(request, 'hiringPlatform/index.html')


def register(request):
    form = CreateUser()
    if request.user.is_authenticated:
        messages.success(request, "User exist already!")
        return redirect('/register')
    else:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "User registered In successfully")
                return redirect('/user_roles')
        context = {'form': form}
        return render(request, 'hiringPlatform/register.html', context)


def loginPage(request):
    form = CreateUser()
    if request.method == 'POST':
        name = request.POST.get('username')
        passwd = request.POST.get('password1')
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "User logged In successfully")
            return redirect('/')
        else:
            messages.error(request, "Wrong username or password")
            return redirect('/loginPage')
    context = {'form': form}
    return render(request, 'hiringPlatform/loginpage.html', context)


def logoutPage(request):
    logout(request, user)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')


def user_roles(request):
    if request.method == 'POST':
        form = UserInterestedRolesForm(request.POST)
        if form.is_valid():
            user_interested_roles = form.save(commit=False)
            user_interested_roles.user = request.user
            user_interested_roles.save()
            return redirect('/job_match')
    else:
        form = UserInterestedRolesForm()
        context = {'form': form}
        return render(request, 'hiringPlatform/jobPage.html', context)


def available_job(request):
    return render(request, 'hiringPlatform/avJobPage.html')


def demoPage(request):
    return render(request, 'hiringPlatform/demoPage.html')
