from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm


# 회원가입
def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('accounts/')

    elif request.method == "GET":
        form = CreateUserForm()

    return render(request, 'signup.html', {'form': form})


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 회원가입과 다르게 맨 앞의 인자로 request가 들어간다.
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('home:index')

        return redirect('accounts:login')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    user_logout(request)
    return redirect('home:index')
