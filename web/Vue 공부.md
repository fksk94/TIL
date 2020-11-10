# Vue Direcive

``` html
<div id ="app">
    
</div>
<!-- Vue CDN 추가 -->
<script>
	const app = new Vue({
        el:'#app', // 어떤 요소를 선택할지
        data: {
            // 뷰에서 사용되는 변수들
            // 다양한 정보와 타입이 딕셔너리 형태로 저장될 수 있다.
        },
        methods: {
            // vue 에서 사용할 함수들을 정의하는 곳
            // 메소드를 정의 할 때는 화살표 함수를 사용하지 않는다. (this)
        }
    })
</script>
```

* v-html

  * innerHTML로 할당
  * HTML을 그대로 읽기 때문에 XSS 공격에 취약

* v-text

  * innerText로 할당
  * {{}}: 보간법, (interpolation)

* v-if, v-if-else, v-else

  * 조건문에 따라서 해당 Tag의 렌더링 여부를 결정.
  * 아예 코드자체가 렌더링 되지 않는다.
  * v-if, v-else 를 사용할 때 사이에 아무 Tag가 있다면 제대로 동작하지 않는다.

* v-show

  * v-show의 값에 따라 css display 속성을 조절해서 화면 노출을 결정.

* v-for

  * 반복문

* v-bind

  * HTML 표준 속성에 Vue의 데이터를 연결

  * `:` 숏컷

  * object 형태(키 = 밸류)로 사용하면 value가 true인 경우만 바인딩 된 값으로 할당 가능

    `class = "{클래스 이름: true(적용) vs false(비적용)}"`

* v-model

  * 양방향 바인딩
  * 입력되어지는 태그(Input, TextArea, Select) 사용

* v-on

  * 이벤트
  * `@`숏컷

* this 정리

  * obj.functionCall() ==> this === obj: 메소드 호출되었을때

  * 그 외 => this === window

    ```js
    const myObj = {
    	myFunc: function () {
    		console.log(this)
    		// 1. 콜백 함수에서 this 를 obj로 만드는 방법(.bind)
            axios.get(URL)
    			.then(function () {
    				console.log(this) //myObj
    		}.bind(myObj))
            
            //2. 콜백 함수에서 this를 obj로 만드는 방법
            axios.get(URL)
    			.then(() => {
                	consol.log(this) // myObj
            })
    	}
    }
    ```