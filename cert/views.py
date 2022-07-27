from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CertPhoneInputForm, CreateUserForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm


# 전화번호 인증 - 인증 정보 받기
def certPhone(request):
    if request.method == "POST":
        form = CertPhoneInputForm(request.POST)
        if form.is_valid():
            nextForm = CertPhoneRecvNumberForm(certType=form.certType,
                                               phone=form.phone.value,
                                               name=form.name.value)

            return render(request, 'certPhoneRecvNumber.html', {'form': nextForm})

    elif request.method == "GET":
        form = CertPhoneInputForm()

    return render(request, 'certPhone.html', {'form': form})


# 전화번호 인증 - 인증번호 받기
def certPhoneRecvNumber(request):
    if request.method == "POST":
        form = CertPhoneRecvNumberForm(request.POST)
        if form.is_valid():
            if form.certType == 1: # 회원가입
                pass
            elif form.certType == 2: # 비밀번호 찾기
                pass
            else:
                return redirect('cert:certPhone')

    return render(request, 'certPhone.html', {'form': form})