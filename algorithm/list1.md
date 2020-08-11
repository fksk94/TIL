# 자료구조

## 1차원 배열의 선언

* 전역, 정적 변수
  * data에 저장
* 참조형 변수
  * heap에서 저장
* 지역 변수
  * stack에서 저장



### 카운팅 정렬

* 각 숫자를 카운트하고 counts에 넣는다.
* 각 숫자들을 카운트 한 것을 인덱스 별로 마지막 인덱스를 설정하여 counts에 넣는다.
* 그리고 배열에 각 숫자를 인덱스 별로 설정한다.
* counts의 각 숫자의 장소에 -1씩 해줘서 인덱스를 설정한다.
* Temp에 새로운 정렬된 리스트를 저장해서 기존의 리스트는 유지한다.
