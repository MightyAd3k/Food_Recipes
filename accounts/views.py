from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect

from accounts.forms import NewUserForm, EditProfileForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('main_page')

        messages.error(request, 'Unsuccessful registration. Invalid information')

    form = NewUserForm()
    ctx = {'register_form': form}
    return render(request, 'register.html', ctx)


def user_profile(request):
    ctx = {'user': request.user}
    return render(request, 'user_profile.html', ctx)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('user_profile')

    form = EditProfileForm(instance=request.user)
    ctx = {'edit_profile': form}
    return render(request, 'edit_profile.html', ctx)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, f"Password has been changed successfully.")
            update_session_auth_hash(request, form.user)
            return redirect('main_page')

    form = PasswordChangeForm(user=request.user)
    ctx = {'change_password': form}
    return render(request, 'change_password.html', ctx)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('main_page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    ctx = {'login_form': form}
    return render(request, 'login.html', ctx)


def logout_request(request):
    logout(request)
    return redirect('/')
