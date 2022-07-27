from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CertPhoneInputForm, CertPhoneRecvNumberForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm
import pdb

# 전화번호 인증 - 인증 정보 받기
def certPhone(request):
    if request.method == "POST":
        form = CertPhoneInputForm(request.POST)

        if form.is_valid():
            nextForm = CertPhoneRecvNumberForm(certType=form.certType,
                                               phone=form.phone.value,
                                               name=form.name.value)

            return render(request, 'cert/certPhoneRecvNumber.html', {'form': nextForm})

    elif request.method == "GET":
        form = CertPhoneInputForm(request.GET)

        certType = request.data.get('certType', default=0)

        # TODO 비로그인 세션 사용이 가능한지 확인해야함.
        # TODO 확인필요. request에 메소드를 따라 render가 전달되는지 확인이 필요하다.
    return render(request, 'cert/certPhone.html', {'certType': form}) # request에 상관없이 certPhone.html에 certType을 심어서 사용


# 전화번호 인증 - 인증번호 받기
def certPhoneRecvNumber(request):
    if request.method == "POST":
        form = CertPhoneRecvNumberForm(request.POST)
        if form.is_valid():
            pdb.set_trace()
            if form.certType == 1: # 회원가입
                pass
            elif form.certType == 2: # 비밀번호 찾기
                pass
            else:
                return redirect('cert:certPhone')

    return render(request, 'cert/certPhoneRecvNumber.html', {'form': form})