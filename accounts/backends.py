from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q
import pdb
import re

User = get_user_model()


class EmailPhoneUsernameAuthenticationBackend(object):
    '''
    식별 우선순위
     1) 전화번호 (한국 전화번호만 한정, '-'없음)
     2) 이메일 (일반적인 이메일 형태만 식별)
     3) 아이디 (알파벳, 숫자로 된 것만 식별)
     타입 식별을 미리하여 UserDb에 한번만 쿼리를 할수 있게 함으로 해서 3번 쿼리를 시도하지 않게 함.
    '''

    def authenticate(self, request, username=None, password=None):
        phonePatt = '^\d{10,11}$'
        emailPatt = '^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$'
        usernamePatt = '^[A-Za-z][\w]+'

        if re.search(phonePatt, username):
            try:
                user = User.objects.get(phone=username)

            except User.DoesNotExist:
                return None

        elif re.search(emailPatt, username):
            try:
                user = User.objects.get(email=username)

            except User.DoesNotExist:
                return None

        elif re.search(usernamePatt, username):
            try:
                user = User.objects.get(username=username)

            except User.DoesNotExist:
                return None

        else:  # 맞는 형식이 없을때
            return None

        if user and check_password(password, user.password):
            return user

        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
