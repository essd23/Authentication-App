from django.contrib.auth.models import User
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, RegisterForm

from verify_email.email_handler import send_verification_email

from .models import Form

from django.core.mail import EmailMessage


def index(request):
    return render(request, 'site_view/index.html')

# Verify Email
def verify_email_message(request):
    return render(request, 'user_auth/email_verify/verify_email_message.html')


def verify_email_complete(request):
    return render(request, 'user_auth/email_verify/verify_email_complete.html')

def verify_email_erorr(request):
    return render(request, 'user_auth/email_verify/verify_email_error.html')


def verify_link_expired(request):
    return render(request, 'user_auth/email_verify/verify_link_expired.html')


def request_new_link(request):
    return render(request, 'user_auth/email_verify/request_new_email.html')

def new_email_sent(request):
    return render(request, 'user_auth/email_verify/new_email_sent.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            inactive_user = send_verification_email(request, form)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            return redirect('verify_email_message')
    else:
        form = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': form})


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user_auth/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {user.username.title()}, welcome back!')
                return render(request, 'user_auth/welcome.html')

        messages.error(request, f'Invalid username or password. Note that both fields may be case sensitive')
        return render(request, 'user_auth/login.html', {'form': form})


def welcome(request):
    return render(request, 'user_auth/welcome.html')


def logout_user(request):
    logout(request)
    return render(request, 'user_auth/logout.html')




























