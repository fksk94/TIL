# Accounts 간단요약

* 앱을 새롭게 생성
* Articles가 이미 존재하지만 Articles는 게시글을 관리하는 역할을 하는 앱
* 이건 회원가입을 관리하는 앱



## 회원 가입 기능 추가

* 회원가입 - DB 유저 정보를 새롭게 추가
* UserCreationForm: djnago 에서 기본적으로 제공해주는 폼
  * 유저 정보를 DB에 저장을 해야함.
  * `from django.contrib.auth.forms import UserCreationForm`
  * 나머지 로직은 CRUD CREATE와 동일

* 회원 가입 후 바로 로그인 ㄱㄱ



## 로그인

* 로그인은 세션을 새롭게 생성
* 쿠키
  * 브라우저에 저장
  * 키-밸류 로 이루어진 작은 데이터 파일
  * 만료일자 가지고 있음
  * 쿠키종류
    * 세션쿠키
      * 사용자가 사이트를 탐색할 때, 설정과 선호 사항을 저장하는 임시쿠키
      * 브라우저를 닫으면 삭제
    * 지속쿠키
      * 사용자가 주기적으로 방문하는 사이트에 대한 설정 정보나 로그인 이름을 유지하기 위해 주로 사용
      * 브라우저를 닫거나 컴퓨터를 재시작해도 남아 있음
* 세션
  * 서버 DB 혹은 메모리
  * 정말 중요한 정보 저장
  * 사용자가 많아지면 서버 느려짐
* AuthenticationForm: Django에서 기본적으로 제공해주는 Form
  * 로그인을 위해서 입력창을 제공
  * 로그인 유효성 검사
  * DB 유저 정보와 비교해서 인증해주는 구조
  * DB를 직접 수정하는 폼이 아니기 때문에 Form
    * 첫번째 인자로 request를 보내야함.
    * 로그인 시, login()과 login 함수의 이름이 같은지 확인
* `return redirect(request.GET.get('next') or 'accounts:index')



## 로그아웃

* 세션을 삭제
* logout 함수: Django에서 기본적으로 제공해 주는 함수
  * 현재 request에서 session에 관한 data를 삭제





## 접근제한

* is_authenticated
  * User 클래스와 AnonymousUser의 속성 값.
    * User 해당값이 항상 True / AnonymousUser는 항상 False
  * 유저의 인증확인
* is_anonymous : 유저가 인증되었는지 확인
* is_superuser: 유저가 최고 관리자인지 확인
* is_staff: 유저가 스태프인지 확인



* login_required 데코레이터
  * 로그인된 유저만 함수를 실행가능하게 만듬
    * accounts/login 으로 리다이렉트해줌
    * next라는 쿼리 문자열이전에 접근하려했던 주소를 keep해줌
      * 킵된 주소를 사용하려면 request.GET.get('next')해서 리다이렉트.
      * `@login_required(login_url='/accounts/test/')`
      * settings.py에 LOGIN_URL을 설정해주면 해당 주소로 갈 수 있음.

* `required_POST` 과 `login_required` 를 같이 사용 못하는 이유.
  * 비로그인 상태로 POST로 logout을 시도했을때,
    * login_required에서 로그인 페이지로 리다이렉트
    * 로그인 완료 후, next를 통해 다시 logout으로 접근
    * 결국 에러발생



## 회원 탈퇴

* 회원 탈퇴는 DB에서 유저정보를 삭제하는 것
* 유저정보는 request.user에 담겨져 있다.
* `data = User.objects.get(id = id)`
* `data.delete()`

* 유저정보는 request.user에 담겨져 있따.
  * request.user.delete()를 하면 유저 정보가 삭제
  * DB정보를 삭제하는 것이기 때문에 POST 요청!



## 회원 정보 수정

* 회원 정보를 Update
* UserChangeForm: Django에서 기본적으로 제공해주는 폼
  * 문제점
    * 일반 유저가 권한설정을 할 수 있다.
    * 우리가 새로 커스텀해야한다.
* `CustomUserChangeForm` 을 만들어서 새로 지정해준다. - UserChangeForm 상속받아야함.
  * 원하는 필드만 수정하게
  * 입력창 보여주기 위해 instance 설정 해주기.



## 비밀번호 변경

* DB를 수정
  * 텍스트 그대로 저장하면 안 됨.
  * 비밀번호 암호화
* **PasswordChangeForm**
  * Form을 상속받아서 정의되어 있음.
  * 첫 번째 인자로 `request.user`가 필요하다.
* 비밀번호 변경 시 로그아웃 되야함
  * 업데이트 해쉬
  * `update_session_auth_hash` 함수로 세션유지함.



* 디버깅 순서
  * 개발 순서 (요청 -> url -> view -> template -> 응답)

  * 개발의 역순으로 디버깅
    * 응답 -> template -> views -> url -> 요청(주소줄 확인, or 장고 log에 찍힌 요청을 확인.)





## url resolver

* resolver는 웹 브라우져에서 요청을 서버로 전달하고 서버에서 주소를 받아 브라우저에 제공하는 기능을 수행
* resolver는 urls.py의 path
* 결과적으로 resolver라는건 실제 주소창에 입력되는 주소와 장고 내부에서 사용하는 url을 서로 번역해주는 역할을 한다.(redirect에서 실행되는 것.)



## Password 암호화

* 보안 시스템이 강한지 약한지 확인하는 방법은 가장약한부분이 얼만큼 강한지에 따라 결정
* PBKDF2
  * 미국 정부시스템에서도 사용
  * NIST에 의해서 인증된 암호화 방식
* 패스워드를 저장하는 방식
  * 있는 그대로 저장
  * 암호화를 시킨다.
    * 단방향 해쉬함수
      * 메시지를 암호화하기는 쉽지만 그 반대는 불가능한 것.
    * 암호화된 해쉬 데이터를 (다이제스트)를 DB에 저장
  * 단방향 해쉬 함수의 문제점
    * 동일한 메세지는 동일한 hash 값을 가지게 됨.
    * 속도가 빨라서 문제.
      * MDS 라는 알고리즘, 1초에 56억번 대입연산할 수 있음.
    * 단방향 해쉬함수 보완
      * salting + 암호화
      * 해쉬함수 여러번 돌림.
      * 반복하는 숫자만 가지고 있으면 할 수 있음.(몇번 돌린지 아니까.)



