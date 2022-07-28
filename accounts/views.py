from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ViewUserForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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

            request.session.set('CERT_DATA', {
                'NAME': form.cleaned_data['name'],
                'PHONE': form.cleaned_data['phone']
            })

            return redirect('cert:certPhoneRecvNumber')

    elif request.method == "GET":
        form = CertPhoneInputForm(request.GET)

    else:
        common.delCertSession(request)
        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    return render(request, 'cert/certPhone.html', {'form': form})


# 회원가입
@require_http_methods(['GET','POST'])
def register(request):
    if not request.session.get('CERT_TYPE') or not request.session.get('CERT_STATUS'):
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)
    elif request.session['CERT_STATUS'] != common.CertStatus.SIGNUP:
        common.delCertSession(request)

        return HttpResponse('<h2>It\'s invalid accessed path.</h2>', status=204)

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'accounts/register_done.html', {})

    elif request.method == "GET":
        form = CreateUserForm()
        form.fields['name'].initial = request.session.get('CERT_DATA').get('NAME')
        form.fields['phone'].initial = request.session.get('CERT_DATA').get('PHONE')

    return render(request, 'accounts/register.html', {'form': form})


# 회원가입
@require_http_methods(['GET'])
def signup(request):
    request.session['CERT_TYPE']    = common.CertType.SIGNUP
    request.session['CERT_STATUS']  = common.CertStatus.CERT_PHONE_INPUT

    return redirect('cert:certPhone') # 전번인증로 넘겨준다.


@require_http_methods(['GET'])
def forgotPassword(request):
    request.session['CERT_TYPE']    = common.CertType.FORGOT_PASSWORD
    request.session['CERT_STATUS']  = common.CertStatus.CERT_PHONE_INPUT

    return redirect('cert:certPhone') # 전번인증로 넘겨준다.


@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 회원가입과 다르게 맨 앞의 인자로 request가 들어간다.
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('index')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
@require_http_methods(['GET'])
def logout(request):
    user_logout(request)
    return redirect('index')


@login_required
@require_http_methods(['GET'])
def myInfo(request):
    if request.method == 'GET':
        form = ViewUserForm(instance=request.user)

    return render(request, 'accounts/myInfo.html', {'form': form})
