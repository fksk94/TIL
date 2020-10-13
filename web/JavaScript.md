# JavaScript

## INDEX

1. [Dom 조작](#Dom 조작)
2. [이벤트 리스너](#이벤트 리스너)
3. [식별자](#식별자 (identifier))
4. [변수](#변수)
5. [타입과 연산자](#타입과 연산자)
6. [조건문과 반복문](#조건문과 반복문)
7. [함수](#함수)
8. [자료구조](#자료구조)
9. [객체](#object (객체 / 오브젝트))
10. [JSON](#JSON ( JavaScript Object Notation ))
11. [Array Helper Method](#Array Helper Method )



## Dom 조작

* 화면으로 표시된 HTML을 조작이 가능.
* `selector`를 이용해서 조작을 한다.
  * `querySelector`를 이용해서 id, class, 태그를 선택해서 조작할 수 있다.
    * `getElementById`는 수업시간에서는 사용하지 않을 예정.
      * live 속성 때문에
* 정리
  1. 선택한다.
  2. 변경한다.



---



## 이벤트 리스너

* 이벤트는 브라우져에서 벌어지는 일

* 특정 이벤트가 벌어지면 특정 행동을 한다. `~하면 ~한다.`

  `이벤트 타겟.addEventListener(이벤트 타입, 할 일)`

* `preventDefault()`

  * 기본 동작을 동작하지 않게 막을 수 있다.



---



## 식별자 (identifier)

- 변수명은 식별자라고도 불림.
- 규칙
  1. 반드시 문자, 달라( $ ) 또는 밑줄로 시작해야 한다 (숫자로 시작 x)
  2. 대소문자를 구분한다
  3. 예약어는 사용 x (const, function, class, ...)
- 스타일 
  - 카멜케이스(lowerCamelCase)
    - 객체, 변수, 함수
  - 파스칼 케이스 (upperCamelCase)
    - 클래스, 생성자
  - 대문자 스네이크 케이스 (UPPER_CASE)



## 변수

- let : 값을 재할당 할 수 있는 변수를 선언하는 키워드

  - 한 번만 선언 ! , 여러 번 할당 할 수 있다.

  ```js
  let x = 1
  x = 3
  ```

  ```js
  // 이 방법은 불가능
  let x = 1
  let x = 3
  ```

  - 블록 유효범위를 갖는다 ( if , for  그리고 함수 등의 중괄호 { } 내부를 의미 )

  ```js
  let x = 1
  if (x === 1) {
  	let x = 2
  	console.log(x) // x = 2 라고 출력됨
  }
  console.log(x) // x = 1이라고 출력됨.
  ```

  

- const : 값이 변하지 않는 상수를 선언하는 키워드

  - 선언 시 반드시 초기 값을 설정해줘야함
  - 초기값을 설정하지 않으면 에러 발생
  - 상수의 값은 재할당 될 수 없고 재선언 될 수 없음 (let이랑 다름)



- var : ES6 이전 변수를 선언하는 키워드
  -  선언도 여러번, 할당도 여러번 가능! 재선언 가능
  -  함수 유효 범위 ( global 유효범위를 가지고 있음 )
  -  BUT , 예기치 않은 문제를 많이 발생시키는 키워드로 웬만하면 사용하지 않는다



**정리**

```js
var // 재할당, 재선언, 함수 스코프
let // 재할당, 블록 스코프
const // 블록 스코프
```



## 타입과 연산자

#### 타입

- number

```js
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8
const e = Infinity // -Infinity 도 가능
const f = NaN // zero error 같은거 10/0 
```

- boolean

```js
const inTrue  = true // 소문자로 표현
const isFalse = false
```

- Empty Value
  - null : 값이 없음을 표현하기 위해서는 **개발자**가 인위적으로 사용하는 값으로 여김 
    - typeof  -> object 
  - undefined : 값이 없을 경우에는 **javascript** 가 할당하는 값
    - typeof  -> undefined
- string
  - 리터럴
    - 리터럴이라는 단어는 값을 프로그램 안에서 직접 지정한다는 의미
    - 리터럴은 값을 만드는 방법

```javascript
const str1 = '홀 따옴표 사용'
const str2 = "쌍따옴표 사용"
str1+str2 // 2개의 문장을 한 문장으로 합침

const str3 = "줄 바꿈은 
허락되지 않는다." 

// escape sequence 
const str4 = "줄 바꿈은  \n 이렇게 해야 한다"


// Template literal 백틱 (``이거)
const str5 = `안녕하세요.
이거얍`

const num = 100
const str6 = `${num} - ${str1}`

```

#### 연산자

- 할당 연산자

```javascript
let c = 0
c += 10
c -= 3
...
c++
c--
```

- 비교 연산자

  - 문자열 비교는 영어 소문자가 대문자보다 큰 값을 가짐. 알파벳은 오름차순으로 순서 비교

- 동등 연산자(' == ')

  - 비교 대상이 서로 다른 타입일 경우, 비교하기 전에 가능하다면 같은 자료형으로 형변환하여 비교 해야함

- 일치 연산자 (' === ')

- 타입과 값이 모두 같은지 비교한다. 동등연산자와 다르게 엄격한 비교를 하기 때문에 일치 연산자를 사용하는 것을 권장한다

- 논리 연산자 

  - && , ||,  ! (not)

- 삼항 연산자

  ```javascript
  const result = Math.PI > 4 ? 'Y':'N'
  console.log(result) // N
  ```



## 조건문과 반복문

#### 조건문

- if, else if, else

- switch

  - 하나의 표현식을 평가하며, 일치하는 항목의 case 절을 실행하는 조건문이다.
  - break 키워드를 통해 switch 문을 벗어난다는 것을 명시
  - break 키워드가 명시되지 않을 경우 switch 문을 벗어나지 못하고 defalut 절까지 실행하게 됨.

  ```javascript
  let name = '홍길동'
  
  switch(name) {
      case 'admin' :{
          console.log('관리자님 환영합니다.')
          break
      }
      case 'manager':{
          console.log('매니저님 환영합니다')
          break
      }
      default:{
          console.log(`${name}님 환영합니다.`)
      }
  }
  ```



#### 반복문

- while (조건)
- for 

```javascript
for (let i = 0; i<6; i++){
    console.log(i) //0 1 2 3 4 5 6
}
```

- for of

  - 배열에서 요소를 하나씩 순회하며 반복하는 반복문이다.
  - 매 요소는 블럭 내에서 새롭게 선언되기 때문에 반드시 변수 선언 키워드를 작성

  ```javascript
  const numbers=[0,1,2,3,4]
  
  for (const number of numbers){
      console.log(number)
  }
  ```

- for in 

  - object의 key를 순회하는 반복문, array의 경우 index 순회

  ```javascript
  const fruits={a:'apple',b:'banana'}
  
  for (const key in fruits){
      console.log(key)
      console.log(fruits[key])
  }
  
  
  // for (value of Object.values(fruits)) list로 반환하기때문에 for of 로 idx순회 
  ```



## 함수

- 함수 선언식

```javascript
add(2,7) //표현식에서는 x
function add (num1,num2) {
    return num1 + num2
}
```

- 함수 표현식 

```javascript
// 익명함수
const sub = function (n1,n2) {
    return n1-n2
}
sub(7,2)
```

```javascript
// 기명함수도 표현 가능
const mysub = function sub (n1,n2) {
    return n1-n2
}
mysub(7,2)
```

- 기본 인자
- 화살표 함수

```javascript
const arrow = function (name) {
    return `hello ! ${name}` 
}
//1. function 키워드 삭제, 화살표 추가
const arrow = (name) => { return `hello, ${name}`}

//2. 매개변수가 하나일 경우 괄호 생략
const arrow = name => { return  `hello, ${name}`}

//3. 함수 바디가 하나의 표현식일 경우 {} & reutrn 생략
const arrow = name => `hello, ${name}`

//4. 단 표현식이 object(dic와 같은 형태) 객체 일 경우 () 안쪽에 객체 표현
const arrow = name => ({ message : `hello, ${name}`})

//
const exam =  () => 'hello,world'


```



## 자료구조

#### Array (배열)

```javascript
const numbers = [1,2,3,4,5]

numbers[0]
numbers[-1] // undefined
numbers.length
```

- reverse

```javascript
numbers.reverse() // [5,4,3,2,1]
```

- push & pop

```javascript
numbers.push('a') //6 => 새로운 배열의 길이
numbers  // [1,2,3,4,5,'a']

numbers.pop() // 'a' 삭제됨 가장 마지막 요소
```

- unshift & shift

```javascript
numbers.unshift('a') //['a',1,2,3,4,5] 추가
numbers.shift() // [1,2,3,4,5] 가장처음요소 지움
```

- includes

```javascript
numbers.includes(1) //true : 안에 1이 포함되어 있는지 확인해줌
```

- index0f

```javascript
numbers.push('a','a')
numbers.index0f('a') // 5 더 앞에꺼 출력
// 존재하지 않으면 -1 출력 
```

- join

```javascript
numbers.join('.') //"1.2.3.4.5.a.a"
```



## object (객체 / 오브젝트)

- 선언

```javascript
const me = {
    name : '홍길동',
    'phone number': '012455667', //두 단어 이상일대 ''
    appleProducts:{
        ipad:'2018pro',
        iphone:'7+',
    }
}
```

- 요소 접근

```javascript
me.name //홍길동
me['name']
me['phone number']
me.appleProducts
me.appleProducts.ipad
```

- object 축약 문법

  - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 아래와 같이 축약 가능

  ```javascript
  const name = '김싸피'
  const score = '80'
  
  const student = {
      name,
      score,
  }
  console.log(student) // {name:'김싸피', score:'80'}
  ```

  ```javascript
  const student = {
      sub : (n1,n2) => n1-n2
  }
  ```

  ```javascript
  let obj = {
      sayhi : function () {
          console.log('hello')
      }
  }
  
  obj.sayhi() //'hello'
  
  
  let obj2 = {
      // 함수의 object 축약형
      sayhi () {
          console.log('hi')
  	}
  }
  obj2.sayhi()
  ```



## JSON ( JavaScript Object Notation )

>javascript object 형태를 가지는 `문자열`

#### object -> json (string)

```javascript
const objData = {
    coffee : 'Americano',
    icecream : 'bravo'
}

const jsonData = JSON.stringify(objData)
console.log(typeof(jsonData))
// "{coffee: "Americano", icecream: "bravo"}"
```

#### JSON -> object

```javascript
const objData2 = JSON.parse(jsonData)
console.log(typeof(objData2)) //object 
//{coffee: "Americano", icecream: "bravo"}
```



## Array Helper Method 

- forEach

  - 주어진 callback 함수를 배열의 각 요소에 대해 한번씩 실행한다
  - 문법

  ```javascript
  arr.forEach(callback(element,index,array)) //index, array 옵션
  ```

  - 사용예시

  ```javascript
  const colors=['red','blue','green']
  
  colors.forEach(function (color){
    console.log(color) //'red,''blue','green'  
  })
  ```

  - exercise

  ```javascript
  const images = [
      { height : 10, width : 30},
      { height : 20, width : 90},
      { height : 54, width : 32},
  ]
  
  const areas=[]
  
  images.forEach(function (image){
      areas.push(image.height*image.width)
  })
  
  //map
  const area = images.map(function (image){
      return image.height * image.width
  })
  console.log(area) //[300,1800,1728]
  ```

- map

  - 배열 내 모든 요소에 대한 주어진 callback 함수를 실행, 함수의 반환값을 요소로 하는 새로운 배열을 반환 (foreach는 x)

  ```javascript
  arr.map(callback(element, index, array))
  ```

  ```javascript
  const nums =[1,2,3]
  
  const doubleNums = nums.map(function (num){
      return num*2
  })
  console.log(duobleNums) //[2,4,6]
  //리턴값으로 새로운 배열을 만들어준다.
  ```

  - exercies

  ```javascript
  const numbers = [4, 9, 16]
  
  const doubleNumbers = numbers.map(function (number){
      return number**0.5
  })
  
  console.log(doubleNumbers)
  ```



- filter 

  - 주어진 callback 함수의 테스트를 만족하는 요소만으로 만든 새로운 배열을 반환. 모든요소

  ```javascript
  const products = [
      { name : 'cucumber', type :'vegetable'},
      { name : 'banana', type :'fruit'},
      { name : 'apple', type :'fruit'},
  
  ]
  const fruit = products.filter(function (product){
         return product.type === 'fruit'
  })
  console.log(fruit) //{name: "banana", type: "fruit"} {name: "apple", type: "fruit"}
  ```

  - exercise

  ```javascript
  const numb = [15,25,35,45,65,44,66,77,86,88]
  
  const num = numb.filter(function (numm){
      if (numm > 50){
          return numm
      }
  })
  ```

- find

  - 만족하는 첫번째 요소를 반환, 값이 없다면 undefined

  ```javascript
  const products = [
      { name : 'cucumber', type :'vegetable'},
      { name : 'banana', type :'fruit'},
      { name : 'apple', type :'fruit'},
  
  ]
  
  const select = products.find(function (s){
      return s.type === 'vegetable'
  })
  ```

- some

  - 배열 안의 하나의 요소라도 callback  함수의 테스트를 만족하면 true를 반환, 아닐경우 false를 반환. 단, 빈배열에서 호출 시 false 반환

  ```javascript
  const products = [
      { name : 'cucumber', type :'vegetable'},
      { name : 'banana', type :'fruit'},
      { name : 'apple', type :'fruit'},
  ]
  
  const someve = products.some(function (product){
      return product.type === 'vegetable'
  })
  
  console.log(someve)
  ```

  

- every

  - 배열 안의 모든 요소가 callback 함수의 테스트를 만족하면 true, 아닐경우 false (빈 배열도)

  ```javascript
  // 하나라도 false 이면 false 임 !
  const users = [
      { id: 21, submmited: true },
      { id: 33, submmited: false },
      { id: 712, submmited: true},
  ]
  
  const hasSubmitted = users.every(function (user){
      return user.submitted
  })
  ```

- reduce

  - 배열의 각 요소에 대해 주어진 callback 함수를 실행하고 하나의 결과 값을 반환
  - reduce는 배열 내의 숫자 총합, 평균 계산 등 배열의 값을 하나로 줄이는 동작

  ```javascript
  arr.reduce(callback(acc,element,idx,array), initialValue)
  ```

  - callback 함수의 첫번째 매개변수 (acc)는 누적 값 전 단계의 결과
  - initialValue 는 반환할 누적 값의 초기 값이다. (없으면 배열의 첫번째 요소가 됨)
  - callback 함수에서 반환하는 값이 누적 값이 된다.

  ```javascript
  const scores = [90, 90, 60, 70]
  
  const totalScore = scores.reduce(function (sum,score){
      return sum + score //sum+=sum+score 
  }, 10000) //function 후에 acc 초기값
  ```

  - exercise

  ```javascript
  const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
  
  const api = {
    'key': 'API_KEY',
    'targetDt': '20200115'
  }
  //key=API_KEY&targetDt=20200115
  
  
  
  const makeUrl =  Object.entries(api).reduce(function (url, api){ //api 배열임
      return url+`${api[0]}=${api[1]}&`
  },baseUrl)
  console.log(makeUrl)
  
  //VM585:4 http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=API_KEY&targetDt=20200115&
  
  ```


* entries

  ``` js
  const object1 = {
    a: 'somestring',
    b: 42
  };
  
  for (const [key, value] of Object.entries(object1)) {
    console.log(`${key}: ${value}`);
  }
  ```

  