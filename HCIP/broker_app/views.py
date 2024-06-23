from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.db import IntegrityError
from .decorators import *
from .models import *


# Create your views here.


def home(request):
    return render(request, 'broker_app/index.html')

@unauthenticated_user
def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'broker_app/login.html')

@login_required(login_url='loginpage')
def dash(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'balance':balance}
    return render(request, 'broker_app/dash.html', context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('firstname')
            messages.success(request, 'Your Account has been created successfully! '+ user)

            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'broker_app/register.html', context)

@login_required(login_url='loginpage')
def bank(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/bnk.html', context)

@login_required(login_url='loginpage')
def crypto(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/crypto.html', context)

@login_required(login_url='loginpage')
def gp(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/gp.html', context)

@login_required(login_url='loginpage')
def otp(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'balance':balance}
    return render(request, 'broker_app/otp.html', context)

@login_required(login_url='loginpage')
def payment(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/payment.html', context)

@login_required(login_url='loginpage')
def payoneer(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/payoneer.html', context)

@login_required(login_url='loginpage')
def paypal(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/paypal.html', context)

@login_required(login_url='loginpage')
def pending(request):
    return render(request, 'broker_app/pending.html')

def reset(request):
    return render(request, 'broker_app/reset.html')

@login_required(login_url='loginpage')
def setting(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'broker_app/setting.html', context)

@login_required(login_url='loginpage')
def skrill(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/skrill.html', context)

@login_required(login_url='loginpage')
def statistics(request):
    return render(request, 'broker_app/statistics.html')


def terms(request):
    return render(request, 'broker_app/terms.html')

@login_required(login_url='loginpage')
def tf(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/tf.html', context)

@login_required(login_url='loginpage')
def transaction(request):
    return render(request, 'broker_app/transaction.html')

@login_required(login_url='loginpage')
def trust_wise(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/trust_wise.html', context)

@login_required(login_url='loginpage')
def LogoutPage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def western_union(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'broker_app/western_union.html', context)