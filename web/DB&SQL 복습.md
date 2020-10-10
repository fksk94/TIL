### DB

* 체계화 된 데이터의 모임
* 자료를 구조화해서 기억시켜 놓은 테이블들의 집합체



### RDBMS(Relational Data Base Manage System)

* 용어 정리
  * 칼럼: 고유한 데이터 형식이 지정되는 열
  * 레코드: 단일 구조 데이터 항목을 가리키는 행
  * 기본키: 각 데이터를 대표하는 고유 값
  * 테이블: 행과 열의 모듈을 사용해서 조직된 데이터 요소들의 집합
  * 스키마: RDB에서 구조와 제약조건을 전반적으로 기술한 명세서.
    * 테이블의 구조, 제약 조건 등을 적어놓은 설계도
* 장점: 만들기 쉽고, 확장이 용이하다.

---



### Sqlite

* `rowid`
  * integer 속성
  * 64비트 `2^64`
  * 사용자가 직접 수정 불가.
  * `autoincrease` 설정을 적용하지 않음.
    * 삭제를 하면 자동으로 숫자를 증가시켜서 이전 pk 값을 사용하지 않는 속성
    * 설정이 안되어 있다는 말은 삭제된 pk 값을 다시 사용한다.
    *  따로 PRIMARY KEY 속성으로 ID를만들게 되면 rowid는 자동 생성되지 않음.
  * 닷 커맨드로 명령어를 수행(.tables, .schema, .database, ...)
    * 이건 sql문이 아니다.

### SQL

* `;`까지 하나의 문장으로 판단. (세미콜론까지)
  * 중간에 엔터를 치던, 공백을 가져가던 하나의 문장은 `;`까지임.
* 소문자, 대문자 구분하지 않지만 대문자 권장
* 주석은 한줄(`--`), 여러줄(`/* */`)



* DDL: 테이블과 관련된 명령어(생성, 수정, 삭제)

  * CREATE(테이블 생성)

    ```sql
    CREATE TABLE 테이블명(
    	컬럼명1 데이터타입 [제약조건],
        컬럼명2 데이터타입,
        ....,
    );
    ```

    * 기본으로 NULL 허용으로 설정되어 있다

    * 데이터타입

      | DATA TYPE               |                                    |
      | ----------------------- | ---------------------------------- |
      | INT or INTEGER          | 정수                               |
      | CHAR(n) or CHARACTER(n) | 고정 길이 n을 가지는 문자열        |
      | VARCHAR(n)              | 최대 길이가 n인 가변 길이의 문자열 |
      | FLOAT(n)                | 부동 소수점 실수                   |
      | DATE                    | 년, 월, 일로 표현되는 날짜 저장    |
      | TIME                    | 시, 분 초로 표현되는 시간          |
      | BLOB                    | 바이너리 값 그대로 저장            |

      

  * ALTER

    ```sql
    ALTER TABLE 테이블명
    RENAME TO 변경할 테이블명;
    
    ALTER TABLE 테이블명
    ADD COLUMN 컬럼명 데이터타입 [제약조건];
    ```

    

  * DROP

    ```sql
    DROP TABLE 테이블명;
    ```

    

* DML: 데이터와 관련된 명령어(생성, 수정, 삭제)

  * SELECT(데이터 조회)

    * DISTINCT: 중복 값을 없애고 결과로 반환

      ```SQL
      SELECT DISTINT director FROM movies;
      ```

    * 산술 연산 검색

      ```sql
      SELECT money * 100 FROM movies;
      ```

    * 조건 검색(WHERE)

      * 기본적인 비교연산자 사용가능(>, <, ==, !=, ....)

      * AND, OR 가능

      * LIKE

        * 와일드 카드 사용
          * `%`: 0개 이상, 있던지 없던지 해당 패턴과 비슷한 값을 돌려줌
          * `_`: 1개, 무조건 해당자리에 어떤 값이 하나가 존재해야 한다.

      * ORDER BY: 정렬(ASC/DESC)

      * GROUP BY

        * 특정 속성의 데이터를 모아서 그룹을 지을 수 있다.
        * `HAVING 조건`: 해당 조건을 만족하는 데이터를 그룹지어 준다.

      * JOIN

        * 두 개 이상의 테이블을 연결해서 하나의 가상 테이블을 만드는 것

        * 분산된 데이터를 하나로 묶어서 쿼리를 할 수 있다.

        * 외래키를 조인 속성으로 이용

          ```sql
          SELECT 결과컬럼, ... FROM 테이블1 [as 별명1]
          [INNER/LEFT/RIGHT/CROSS] JOIN 테이블2 [as 별명2]
          ON 연결 조건 / USING 일치컬럼
          [GROUP BY]
          [ORDER BY];
          ```

          * INNER 속성
            * 가장 많이 쓰이는 JOIN
            * 교집합! 서로 공통되는 것을 결합하여 테이블로 표현
          * LEFT, RIGHT
            * 테이블 순서에 따라서 합침.
            * 값이 없을 때는 NULL을 채워서 연결시켜줌.
          * CROSS
            * ON이나 USING으로 한정하는 필드가 없으면, N X M 개의 행을 가진 모든 조합을 만들어냄.

      * 서브쿼리

        * SELECT 안에 SELECT를 내포하고 있는 형태.

        * 내포된 SELECT가 상위 SELECT보다 먼저 수행.

          ```SQL
          -- 컬럼에 내포하고 있는 형태
          SELECT movie.name, director, (SELECT AVG(balance) FROM theaters)
          FROM movies;
          
          -- FROM과 WHERE에서도 마찬가지로 사용가능.
          ```

          

  * * INSERT (데이터 생성)

      ```sql
      INSERT INTO 테이블명 [(컬럼명1, 컬럼명2, ...)](컬럼 리스트라고 하겠습니다.)
      VALUES (컬럼1에들어갈데이터, 컬럼2에들어갈데이터 , ....)[, (속성 값들2), (속성 값들3)];
      ```

      * 컬럼 리스트는 생략 가능하며, 생략한 경우는 테이블을 정의할 때 컬럼의 순서대로 VALUES 에 속성 값을 적어줘야 함.
      * rowid 를 사용하면 컬럼 리스트를 새략해도 id 값을 따로 입력하지 않아도 되는데 
        * 따로 ID를 정의한 경우는 id 값을 넣어줘야 함.

    * UPDATE (데이터 수정)

      ```sql
      UPDATE 테이블명
      SET 컬럼명=수정값 [, 컬럼명2=수정값]
      [WHERE 조건];
      ```

      * WHERE이 없으면 모든 레코드를 수정.

      

    * DELETE (데이터 삭제)

      ```sql
      DELETE FROM 테이블명
      [WHERE 조건];
      ```

      * WHERE이 없으면 모든 레코드를 삭제.

      

  * DCL : 데이터 베이스와 관련된 명령어 (접근권한)

    * DB 사용자에게 특정 권한을 수여 / 회수
    * GRANT
    * REVOKE
    * COMMIT
    * ROLLBACK
    * SAVEPOINT



---

## ORM

* 모든 정보 조회

  ```python
  Article.objects.all()
  ```

  * data object가 QuerySet으로 전달 되어짐

  ```python
  SELECT * FROM articles;
  ```

  * Table 정보가 전달 되어짐.

* 테이블 생성

  ```python
  class 테이블명(models.Model):
      컬럼명1 = models.데이터타입필드([제약조건, 속성, ...])
      컬럼명2 = models.데이터타입필드([제약조건, 속성, ...])
      ....
  	
      def __str__(self):
          return self.컬럼명1
  ```

  * `python manage.py makemigrations` : migrations 파일 생성(설계도 생성)
  * `python manage.py migrate`: 설계도를 기반으로 DB에 테이블 생성



* 데이터(레코드) 생성

  * 3가지 방법

    * ```python
      board = Board() # 인스턴스 생성
      board.title = '제목'
      board.content = '내용'
      board.save() # DB에 저장
      ```

    * ```python
      board = Board(title='제목', content='내용')
      board.save() # DB에 저장
      ```

    * ```python
      board = Board.objects.create(title='제목', content='내용') # DB에 정보저장
      ```



* 데이터 조회

  * `.get(조건)`: 찾는 값이 1개만 있을 때, (1개 이상이 나오게 되거나 값이 없으면 오류)

  * `.filter(조건)`: 값이 있던 없던 데이터를 QuerySet으로 리턴.

  * 특정 조건에 따른 ORM 작성

    * 전체 길이, 인원 수, 갯수 : 갯수를 세려는 QuerySet에 `.count()` 호출

    * 조건을 검색할 때 Queryset field Lookup 사용.

      * 크거나 같을 때(`__gte`)
      * 여러 개가 있다. 공식문서 확인.

      * https://docs.djangoproject.com/ko/3.1/topics/db/queries/

  * Q object

    * 조건을 캡슐화 사용 가능.

    * AND 는 `,`로 표현이 가능한데 OR 표현은 `|`로만 표현할 수 없다.

      ```python
      Person.objects.filter( Q(age__lte=20) | ~Q(last_name='Park'))
      ```

      * `~`로 NOT 표현을 할 수 있다.

  * 특정 칼럼만 보고 싶을 때 `.values()`

    ```python
    Person.objects.filter(age=20).values('name', 'age')
    [{'name': 'ed', 'age':20}]
    ```

  * 정렬

    * `order_by('컬럼명')`
      * `-`부호로 내림차순 설정 가능
      * `?`: 랜덤하게 정렬(매우느림)

  * LIMIT, OFFSET

    * LIMIT : 갯수제한 (슬라이싱으로 ORM에서 표현[:10])
    * OFFSET : 특정 인덱스 정보(인덱싱으로 ORM에서 표현.) 배열로 표현 ([0]이렇게)
      * ORM도 0부터 시작 - 주의!!

  * aggregation

    * 집계함수
    * Avg, Count, Min, Max 등(첫문자 대문자인 것 확인)
    * aggregate: 계산 후 딕셔너리로 그 값을 반환
    * annotate: 계산 후 결과에 컬럼을 새롭게 추가해서 그 값을 보여줌.



* 데이터 삭제
  * 삭제하려는 데이터 object에서 delete() 호출해주면 됨.



### 1:N

* ForeingKey

  * 필수 인자 2개

    * 참조하는 객체
    * `on_delete` 속성 : 삭제될때 참조데이터의 처리 결정
      * CASCADE: 참조객체 같이 삭제
      * PROTECT: 참조하는 객체가 있으면 삭제 불가하게 설정.
      * SET_NULL: 참조하는 객체가 삭제되면 그 값을 NULL로 변경
      * SET_DEFAULT: 참조하는 객체가 삭제가 되면 그 값을 default 값으로 변경. default 값을 설정해야한다.

  * `필드이름_id`컬럼이 생성된다.

  * 역참조

    * 부모가 어떤자식을 가지고 있는지 참조하는 형태

    * `자식테이블명_set` 접근가능

    * 몇개의 자식테이블이 있는지 모르기 때문에 다이렉트로 접근 불가

      `parent.child_set.name` 이렇게 X

      * 접근하려면 for문을 사용하거나 filter로 조건을 준 후 indexing으로 접근.





### N:M

* ManyToManyField

  * 필드가 생성되는 것이 아니라 테이블이 생성된다.

    `앱이름_모델이름_필드이름`

    * 필드 이름 생성 규칙

      * 서로 다른 테이블간의 N:M

        ```
        참조하는모델_id
        참조당하는모델_id
        ```

      * 같은 테이블 간의 N:M

        ```
        from_모델명_id
        to_모델명_id
        ```

        

  * 필수 인자: 참조하는 객체

  * related_name: 역참조 할 때 이름을 설정하는 속성

    * 역참조 이름을 설정하게 되면 더이상 `_set`으로 접근 불가
    * 특정한 상황에서는 `related_name`이 필수.
      * 두 테이블에서 두 개 이상의 관계설정이 있을 경우 필수!!
        * User와 Article간의 1:N 관계와 N:M의 좋아요 관계가 있을 때 하나는 `related_name`이 설정되어 있어야 역참조가 중복되지 않는다.

  * Through: 중계 테이블을 정의해서 사용할 때 중계 테이블을 등록

  * symmertical : 대칭적으로 간주해서 동시에 참조하는 속성 (친구와 팔로우 관계)

  * 값을 추가 할 때는 add / 값을 삭제 할 때는 remove