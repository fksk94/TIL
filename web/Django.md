# Django

python를 기반으로 하는 백엔드 프레임워크

### 설치 방법 

pip install Django

Django admin startproject (프로젝트명)

Django manage.py startapp (앱명-복수형지향)

앱생성 후, 필히 settings 파일안에 등록해야 됨.

한국어 설정, 타임존 설정



### 프로젝트 흐름

#### MTV 패턴 /  MVC 패턴

MODEL, Template, View

MODEL, View, Controller



View가 되게 헷갈릴 수 있다. 하지만 Django에서는 Control은 view가 한다는 것을 잊지말자.



이 순서로 설정

urls.py

views.py

models.py



Template variable

- views.py에서 템플릿 형태로 옮겨서 사용
- render에서 세번째 인자로  dict형태로 주면 됨.
- 그러면 {{key}} 형태로 사용가능



동적 라우팅 - 주소일부에 변수처럼 값을 설정해서 전달하는 형식

여러 사용자, 여러 페이지를 보여주기 위해 사용



django url dispatcher를 검색해서 변수로 사용할 수 있는 타입을 보여준다.

slug ==> 문자 숫자 밑줄 하이픈 만을 포함.

로직 {%%}

값 {{}}

주석 {##}, <--! -->

#을 쓰는게 좋음. 

``` html
<%  for menu in menus %>
    <p>{{forloop.counter}} {{menu}} </p>
<% empty %>
    <p>
        비었을때
    </p>
<% endfor %>
```

``` django
<% if 조건 %>
<% elif 조건 %>
<% else %>
<% endif %>    <# 조건연산자 사용가능 #>
```

밑에 클릭해보면 됨.

<Form>
    <input type="text" name="name">
    <input type="submit"> <# 버튼이랑 다름! #>
</form>



데이터를 보내려는 목적지 주소

action = url

localhost::catch형태

/catch/ -> local 호스트에서 주소 입력

catch/ -> 현재에서 주소 입력



method GET, POST 형식

GET 방식은 정보를 조회할 때

전달되어지는 데이터 / 데이터의 값.

&로 구분되어 날라감.

