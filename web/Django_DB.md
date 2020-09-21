# 1:N 관계

- 장고 모델에서 사용되는 Field
  - 1 : 1 : OneToOneField() -> 유저와 프로필
  - 1 : N : ForeignKey() -> 글과 댓글, 제조사와 자동차
  - N : M : ManyToManyField()
- ForeignKey 사용법
  - 언제 사용?
    - 맛집 - 리뷰 / 지역 - 관광명소 등등
  - 사용 방법
    - models.ForeignKey(참조 모델, 참조모델이 삭제되었을 때 어떻게 할지)
      - `models.ForeignKey(Articles, on_delete=models.CASCADE)`
        - on_delete 종류
          - CASCADE : 참조하는 테이블이 삭제되면 내 데이터도 삭제
          - PROTECT : 참조하는 테이블이 삭제되려고 하면 삭제하지 못하게 에러를 발생
            - 참조(1의 입장) 테이블을 삭제하려면 N 입장의 테이블의 관계 정리가 필요
          - SET_NULL : 참조하는 테이블이 삭제되면 내 데이터에 해당 값을 NULL로 설정
            - 이 값을 사용하려면 null-True가 필요하다
          - SET_DEFAULT : 참조하는 테이블이 삭제되면 Default 값으로 설정
          - SET(함수명) : 특정 함수를 호출해서 그 함수의 결과 값으로 설정
          - DO_NOTHING : 아무것도 하지 않음
    - 참조 모델이 DB에 저장될땐는 pk 값을 저장함
      - 그 칼럼명은 필드명_id 라고 장고에서 만들어 줌





Shell_plus 사용

* 댓글을 달 수 있는 인터페이스 사용
* 쉘플러스는 파이썬 환경 -> python 코드 -> 쟝고에 활용 가능

