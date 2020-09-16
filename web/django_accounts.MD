라이브 진행

- accouts라는 앱을 생성
  - 동일하기 urls 분리
  - models.py는 장고에서 제공하는 USER  사용하기 떄문에 따로 정의는 하지 않음.
  - form도 장고에서 제공하는 form을 사용하기 때문에 따로 정의는 하지는 않음.
    -  but, custom 해야함.

***



- 회원가입

  - Authentication(인증) : 신원확인. 유저가 '나는 이러한 사람이다.'라고 신원 확인
  - Authorization(권한,허가) : 권한을 부여 

  - 회원 가입 => 새로운 유저를 받겠다. => 유저 정보를 받아서 DB에 생성(CREATE)

    - UserCreationForm : 장고가 제공하는 Form

      - 입력받은 USER 정보를 최종적으로 DB에 저장.
      - ModelForm

      ```python
      from django.contrib.auth.forms import UserCreationForm #암기하기
      
      
      def signup(request):
          if request.method == 'POST:
          	form=UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  return redirect('articles:index')
          else:
          	form = UserCreationForm()
          context={
              'form':form,
          }
          return render(reqeust,'accounts/signup.html',context)
      ```

      

- 로그인

  - 새롭게 세션을 만드는 동작(Create)
  - **쿠키**
    - 브라우저 저장이 되는 내용
    - 키 = 밸류의 적은 데이터 파일
    - 만료날짜, 경로정보
    - 쿠키가 세션보다 속도가 빠름.
    - 보안은 세션이 더좋음. 쿠키는 브라우저 저장이 되기 때문에 타인이 볼 수 있음.
    - 종류
      - 세션쿠키
        - 쇼핑몰 장바구니
        - 브라우저를 닫으면 삭제됨.
      - 지속쿠키
        - 24시간 동안 닫기. 로그인 이름 유지
        - 로컬에 저장이 되서 컴퓨터를 재시작해도 남아 있음.
        - 일정 기간이 지나면 만료날짜가 지나고 삭제됨. 자주 입력하면 날짜가 연장되면서 남아있음.
  - **세션**
    - 서버에 DB, 메모리 
    - 특정 사용자의 중요한 정보
    - 사용자가 많아지면 서버 메모리를 많이 사용하게 되어 정말 주용한 정보만 저장.
  - 세션에 담긴 유저 정보가 특정 브라우저를 사용하는 유저가 맞는지 확인하기 위해서 세션 키(id)를 쿠키에 전달을 해줌.
  - 브라우저에서 쿠키를 삭제한다면?
    - 서버는 해당 브라우저의 유저가 누구인지 확인 할 수 없게 됨.
    - 새롭게 로그인을 해서 새로운 세션키를 발급받아야 함. 쿠키 새롭게 생성됨.

  ​	

  -  AuthenticationForm

    - 장고에서 제공해주는 form
    - 로그인에서 필요한 정보를 받아서 유효성 검사하고 회원인것도 확인.
    - 따로 DB에 저장하는 것이 아니어서 Form
    - 첫번째 인자로 `request` 들어가는 걸 확인.

  - 실질적으로 로그인을 하는 함수는 장고에서 제공해주는 login 함수

    - 회원임이 확인되면 세션을 생성.

    ```python
    # views.py
    from django.contirb.auth.forms import AuthenticationForm
    from django.contrib.auth import login as auth_login # def login 이름이랑 겹쳐서 재귀현상으로 에러 발생. 이름 변경
    
    def login(request):
        if request.method=='POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                auth_login(request, form.get_user()) # 장고에서 제공해주는 함수
                return redirect('articles:index')
        else:
        	form = AuthenticationForm()
            
        context = {
            'form':form,
        }
        return render(request,'accounts/login.html',context)
    ```

    

***

기존주소/login

- 접근제한
  
  - request에 로그인 정보가 들어있음. user
  
  - request.user
  
  - `request.user.is_authenticated`
  
    - 로그인 여부 확인
    - `is_superuser`: 현재 로그인한 유저가 관리자인지 아닌지 여부 확인
    - `is_anonymous`: 로그아웃 여부
  
  - 데코레이터
  
    - login_required
  
      ```python
      from django.contrib.auth.decorators import login_required
      
      @login_required
      def update(request):
          pass
      ```
  
    - 로그아웃상태에서 update로 접근을 했다면
  
      - /account/login/?next=/accounts/update/로 주소가 나타나는 것을 확인 가능
      - 이 주소 형식은 전형적인 GET 타입의 querystring
      - request.GET.get('next') 하면 /accounts/update/를 획득할 수 있다.
      - redirect(request.GET.get('next') or 'articles:Index')로 이동할 수 있음.



---

* 회원탈퇴
  * urls.py를 정의한다. 회원탈퇴요청이 들어오면 views에서 함수를 실행하게 정의.
  * views.py에서 삭제하는 함수를 정의
    * 회원 가입 -> DB에 유저 정보를 생성.
    * 회원 탈퇴 -> DB에서 유저 정보를 삭제.
    * 유저 정보를 delete() 실행하면 삭제됨.
      * 유저정보는 어디에 위치해 있나?
        * request.user 에 있음.
        * request.user.delete() 하면 DB에서 삭제됨.
    * 여기에서 생각해보면 로그인하지 않은 유저가 요청을 하면 되지 않음.
      * 로그인 되었을 때만 회원 탈퇴가능 하게 is_authenticated로 접근 제한.

---

* 회원정보수정

  * UserChangeForm 사용

    * 관리자 수정페이지 나옴.

  * Custom해서 사용해야 한다.

    * forms.py에서 CustomUserChangeForm을 정의

      * UserChangeForm을 상속받아서 정의

        ``` python
        from django.contrib.auth.forms import UserChangeForm
        from django.contrib.auth import get_user_model
        
        class CustomUserCreationForm(UserChangeForm):
        
            class Meta:
                model = get_user_model()
                fields = ('email', 'first_name', 'last_name')
        ```



---

* 비밀번호 / 패스워드 changeform 사용하면 되는데, 이거 커스텀도 해야한다.