# Django 정리

## Model

* DB에 데이터를 저장하고 가져오는 것

* SQL (select * from table;)

* ORM(쉽게 말해서 통역기)

  * 쿼리를 python에서 object로 사용할 수 있게 해줌.

* models.py에 모델 클래스를 정의해서 사용할 수 있음.

  * class 테이블명(models.Model) :

    title = models.CharField(max_length=100);

    * 자주사용하는 필드명
    * CharField / DateTimeField / TextField / IntegerField / BooleanField / ...
    * Model field라고 구글링하면 다 찾음



* 클래스를 다 정의하면 반드시 해야하는 일!!
  * makemigrations
    * python manage.py makemigrations 앱이름
    * DB에 적용하기 위한 설계도 제작
    * app 이름을 뒤에 적으면 해당 app에 있는 models.py의 내용만 설계도를 만듬.
  * migrate
    * python manage.py migrate 앱이름
    * 만들어진 설계도를 가지고 DB에 테이블을 생성.
    * app 이름을 적으면 해당 app에 있는 migration 파일을 db에 적용시킴.
  * showmigrations
    * 확인..?
  * sqlmigrate
    * 해당 테이블 확인



## DB 사용

* DB api

  ``` python
  모델클래스이름.objects.QuerySetAPI
  
  Article.objects.QuerySetAPI #objects <- s 조심
  ```

  