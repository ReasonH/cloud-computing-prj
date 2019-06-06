from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from web import s3_interface
from web.forms import CreateUserForm

def signin(request, path = ''):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('file_list', path = path)
        else:
            return redirect('home')

def signup(request, path = ''):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            s3_interface.make_directory(s3_interface.BUCKET, user.username, 'waste/')
            return redirect('file_list', path = path)
        else:
            return redirect('home')

@login_required
def delete_account(request):
    if request.method == 'GET':
        return render(request, 'registration/delete_account.html')
    elif request.method == 'POST':
        if request.POST.get('yes'):
            return redirect('delete_account_success')
        else:
            return redirect('/')

@login_required
def delete_account_success(request):
    if request.method == 'GET':
        # delete account
        u = User.objects.get(username = request.user.username)
        u.delete()
        # logout
        logout(request)
        return render(request, 'registration/delete_account_success.html')

