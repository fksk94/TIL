# Django 필요한 표현

* 프로젝트 만들기
  * django-admin startproject first_project

* 앱 만들기 후 settings에 설정.
  * python manage.py startapp articles

* 서버 실행
  * python manage.py runserver

* 뷰함수의 첫번째는 request 필수
  * def index(request):

* 코드작성 순서
  1. urls.py
  2. views.py
  3. templates.py





# Django 정리

* 설치

  `pip install django`

* 시작

  `django-admin startproject first_webex`

  * first-webex 라는 폴더가 생성

    * 안에 manage.py 생성 및 설정파일 폴더 생성

      `python manage.py '장고명령어'`

* 장고 프로젝트는 app의 집합체

  * 실제로 어떠한 역할을 말해주는 app
  * 하나의 프로젝트는 여러개의 app을 가짐
    * app : 하나의 역할 및 기능 단위로 쪼개진 형태
      * ex) 회원관리 / 글작성 / 데이터 수집 등등
      * 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 됨.
      * 나누는게 좋긴하지

* 앱 만들기

  `python manage.py startapp articles`

  * articles 라는 앱 폴더 생성

* 앱 설정하기

  * settings.py 안에 INSTALLED_APPS 안에 'articles' 설정.

* 서버 실행

  `python manage.py runserver`

* 뷰함수의 첫번째는 request 필수

  ``` python
  def index(request):
      #render에도 필수
      pick = render(request, 'something')
      return pick
  ```

* 기타 설정 : 대/소문자 주의

  * LANGUAGE_CODE = 'ko-kr'
* TIME_ZONE = 'Asia/Seoul'
  
* {% comment %} {% endcomment %}

  * 주석처리