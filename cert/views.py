from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import CertPhoneInputForm, CertPhoneRecvNumberForm, ChangePasswordForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login as user_login
from django.template import Template
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponse
from django.contrib.auth.password_validation import password_changed
from django.views.decorators.http import require_http_methods
from ably import common
import pdb


# 전화번호 인증 - 인증정보 입력
@require_http_methods(['GET','POST'])
def certPhone(request):
    if not request.session.get('CERT_TYPE') or not request.session.get('CERT_STATUS'):
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)
    elif request.session['CERT_STATUS'] != common.CertStatus.CERT_PHONE_INPUT:
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)


    if request.method == "POST":
        form = CertPhoneInputForm(request.POST)

        if form.is_valid():
            request.session['CERT_STATUS'] = common.CertStatus.CERT_PHONE_RECV_NUMBER

            request.session['CERT_DATA'] = {
                'NAME': form.cleaned_data['name'],
                'PHONE': form.cleaned_data['phone']
            }

            return redirect('cert:certPhoneRecvNumber')

    elif request.method == "GET":
        form = CertPhoneInputForm(request.GET)

    else:
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    return render(request, 'cert/certPhone.html', {'form': form})


# 전화번호 인증 - 인증번호 받기
@require_http_methods(['GET','POST'])
def certPhoneRecvNumber(request):
    if not request.session.get('CERT_TYPE') or not request.session.get('CERT_STATUS'):
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    elif request.session['CERT_STATUS'] != common.CertStatus.CERT_PHONE_RECV_NUMBER:
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)


    if request.method == "POST":
        form = CertPhoneRecvNumberForm(request.POST)
        if form.is_valid():

            if request.session['CERT_TYPE'] == common.CertType.SIGNUP:
                request.session['CERT_STATUS'] = common.CertStatus.SIGNUP

                # 회원가입시 유저가 있는지 체크
                phone = request.session['CERT_DATA']['PHONE']

                userModel = get_user_model()
                rstUser = userModel.objects.filter(phone=phone)
                if rstUser:
                    user = rstUser[0]
                    common.delCertSession(request)
                    return render(request, 'cert/userFound.html', {'username': user.username})

                return redirect('accounts:register')

            elif request.session['CERT_TYPE'] == common.CertType.FORGOT_PASSWORD:
                phone = request.session['CERT_DATA']['PHONE']

                # 비밀번호 재설정시 유저가 있는지 체크
                userModel = get_user_model()
                rstUser = userModel.objects.filter(phone=phone)
                if not rstUser:
                    common.delCertSession(request)
                    return render(request, 'cert/userNotFound.html', {})
                
                request.session['CERT_STATUS'] = common.CertStatus.CHANGE_PASSWORD

                return redirect('cert:changePassword')

    elif request.method == "GET":
        form = CertPhoneRecvNumberForm(request.GET)

    else:
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    return render(request, 'cert/certPhoneRecvNumber.html', {'form': form})


# 비밀번호 재설정
@require_http_methods(['GET','POST'])
def changePassword(request):
    if not request.session.get('CERT_TYPE') or not request.session.get('CERT_STATUS'):
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)
    elif request.session['CERT_STATUS'] != common.CertStatus.CHANGE_PASSWORD:
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)


    if request.method == "POST":
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            # 유저패스워드 변경
            phone = request.session['CERT_DATA']['PHONE']

            userModel = get_user_model()
            rstUser = userModel.objects.filter(phone=phone)

            if not rstUser:
                common.delCertSession(request)
                return render(request, 'cert/userNotFound.html', {})

            user = rstUser[0]
            password = form.cleaned_data['password1']

            user.set_password(password)
            user.save()

            common.delCertSession(request)

            return render(request, 'cert/changePassword_done.html', {})

    elif request.method == "GET":
        form = ChangePasswordForm(request.GET)

    else:
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    return render(request, 'cert/changePassword.html', {'form': form})