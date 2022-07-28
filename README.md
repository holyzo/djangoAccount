# 설치방법 (윈도우 기준)
1. > git clone https://github.com/holyzo/djangoAccount.git
2. > djangoAccount\venv\scripts\activate.bat
3. > cd djangoAccount
4. > pip install -r requirements.txt
5. > python manage.py runserver
6. 브라우져에 "http://127.0.0.1:8000/index" 페이지로 이동한다.

# 구현스펙
- python 3.9
- django 4.0
- django-bootstrap4

# 페이지 구조
- index/ 홈
  - 회원가입 기능
  - 로그인 기능
    - 비밀번호 재설정 기능
  - 로그아웃 기능 (로그인시 보임)
  - 회원 정보 보기 기능 (로그인시 보임)

# 프로젝트 설명
- 로그인 시 (username, 폰번호, 이메일 식별 우선순위)
  * 타입 식별을 미리하여 UserDb에 한번만 쿼리를 할수 있게 함으로 해서 3번 쿼리를 시도하지 않게 함.
  1. 전화번호 (한국 전화번호만 한정, '-'없음) 
  2. 이메일 (일반적인 이메일 형태만 식별)
  3. 아이디 (알파벳, 숫자로 된 것만 식별)
# 기능 확인 방법
1.회원가입 번호인증은 아래와 같이 진행됩니다.
1) 홈 -> "signup" 클릭 
2) 인증정보 입력 후 "submit" 클릭 
3) 인증번호 6자리 아무거나 입력후 "certificate" 클릭 (존재하는 폰번호가 있을 경우 아이디를 알려주며 로긴화면으로 리다이렉션)
4) 회원가입 정보 입력 후 "Register" 클릭 
5) 가입 완료 페이지

2.비밀번호 재설정 번호인증은 아래와 같이 진행됩니다.
  1) 홈 -> "login" 클릭
  2) "forgot password" 클릭
  3) 인증정보 입력 후 "submit" 클릭
  4) 인증번호 6자리 아무거나 입력후 "certificate" 클릭 (폰번호가 존재하지 않을 경우 계정이 없다고 알려주며 홈화면으로 리다이렉션)
  5) 변경할 패스워드 입력 후 "Change password" 클릭
  6) 변경 완료 페이지

3.내 정보 보기는 아래와 같이 진행됩니다.
  1) 홈(로그인 상태) -> "my information" 클릭
  2) 내 정보 보기 페이지