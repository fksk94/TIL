# 0813 아침복습

* Float
* Flex
* Grid
* Bootstrap



## Float

* 한 요소가 정상흐름으로 부터 빠져 텍스트 및 인라인 요소가 그 주위를 감싸는 자기 컨테이너의 좌, 우측을 따라 배치되어야 함을 지정
* clear
  * 선행 floating 요소가 그 아래로 내려가야 하는지(normal flow로 돌아가는)를 지정할 때 사용되는 속성
* flex box 및 그리드 레이아웃과 같은 기술이 나오기 전에 float은 열 레이아웃을 만드는데 사용되었다.
* mdn에서는 더 새롭고 나은 레이아웃기술(flex, grid) 나와서 현재 레거시한 레이아웃 기술로 분류
* 결국은 텍스트 블록 내에서  float  이미지를 위한 역할로 들어감.
* 그래도 네이버에서는 여전히 사용되고 있음을 확인할 수 있음.



## Flex (Flexibl box module)

* flex 인터페이스 내의 아이템 간 공간 배분과 정렬 기능을 제공하기 위한 1차원 레이아웃 모델
* 축
  * justify: main 축(default: 좌 -> 우)
  * align: cross축
  * content: 여러 줄을 설정
  * itmes: 한 줄 설정
  * self: 개별요소 설정
* display: flex
  * 정렬하려는 부모 요소에 선언
  * inline-flex
* flex-direction
  * 쌓이는 방향을 설정
  * row(default) : 좌 -> 우
  * row-reverse: 우 -> 좌
  * column: 위 -> 아래
  * column: 아래 -> 위
* justify-content
  * 메인 방향축 요소들을 어떻게 배치할지 설정
  * flex-start(기본 값): 좌 상단부터 시작하므로 좌측 상단부터 차례로 배치됨.
  * flex-end: 끝나는 점 부터 배치(아이템의 순서는 그대로 정렬만 우측)
  * center: 메인축 정중앙
  * space-between: 좌우 정렬(양 끝 아이템은 양끝에 배치하고 균등하게 아이템을 위치)
  * space-around: 아이템 좌우에 동일한 공간을 부여
  * space-evenly: 균등 정렬

* align-items
  * cross 축 요소를 어떻게 배치할지 결정
  * 기본값 : strech - 공간을 아이템으로 가득 채움
  * flex-start, flex-end, center
  * baseline: item 내부의 text 밑을 기준선으로 맞춤.
* align-self: cross 축 각 개별 아이템을 어떻게 배치할 지 결정.
  * 설정 값은 위와 동일 (기본값: auto)
* order
  * 정렬
  * 기본 값: 0(모든 아이템)
  * 작은 숫자일수록 앞에 배치
* flex-grow: 메인 축에서 남는 공간을 각 항목에게 분배하는 방법
  * 각 아이템에 값을 줘서 그 공간만큼 할당
  * 각 아이템의 비율을 설정하는게 아님
  * 음수는 불가능



## Bootstrap

* 트위터에서 시작된 오픈 소스 프론트엔드 라이브러리? 프레임워크!
* 웹 페이지에서 쓰는 많은 요소를 거의 내장
* 디자인할 시간을 줄여주고, 여러 웹 브라우저를 지원하기 위한 크로스 브라우징에 효과적
* 웹 브라우저 크기에 따라 자동정렬되는 그리드 시스템
* 반응형 웹 디자인
* 그리드 시스템
  * flexbox를 기반으로 12개의 column 시스템을 가짐
  * 12개가 약수가 제일 많아서 이거 선택.
  * container > row > col

* prefix
  * 부트스트랩에서  px 확인
  * 이름 밑에 있는 창크기 기억  ex) 576(sm)