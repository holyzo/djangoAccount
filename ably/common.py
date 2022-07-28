from enum import IntEnum, auto

# 공용 상수

# REGEX 패턴
PATT_PHONE                      = r'^\d{10,11}$'
PATT_EMAIL                      = r'^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$'
PATT_USERNAME                   = r'^[A-Za-z][\w]+'
PATT_SOCIAL_SECURITY_NUMBER_PRE = r'^\d{6}$'

# 인증 타입
class CertType(IntEnum):
    SIGNUP = 1
    FORGOT_PASSWORD = 2

# 인증 상태
class CertStatus(IntEnum):
    INIT                    = 0
    CERT_PHONE_INPUT        = auto()
    CERT_PHONE_RECV_NUMBER  = auto()
    SIGNUP                  = auto()
    CHANGE_PASSWORD         = auto()

def delCertSession(request):
    if request.session.get('CERT_TYPE'):
        del request.session['CERT_TYPE']
    if request.session.get('CERT_STATUS'):
        del request.session['CERT_STATUS']
    if request.session.get('CERT_DATA'):
        del request.session['CERT_DATA']