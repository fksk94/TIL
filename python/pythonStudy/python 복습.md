# python 복습!



## jpyter 00

### print

``` python
# 행을 바꾼 것을 붙여서 출력한다.
print('a\
as')

# 행을 바꾸어 바꾼 상태 그대로 출력한다.
print('''asd
asdas
asdasd''')
```

### 주소, 값 할당

```python
id(x) # 이 함수로 주소를 확인가능
```

* 리스트의 경우, x라는 전체 리스트를 가리키는 주소는 다르다. ex) 9124124
* 리스트 안의 요소도 다르다. ex) 2084022208
* 리스트 안의 요소는 16씩 증가하는 주소를 가진다.



``` python
x = y = 1004 # 이처럼 한번에 할당 가능.
x, y = 1, 2 # 이거는 가능한데.
x, y = 1, 2, 3 # 불가능.
x, y, z = 1, 2 # 불가능.
x, y, z = 1 # 불가능.
x = 1, 2, 3 # 튜플 형식으로 가능
```



* 할당할 시, 주의 점이 있다.
* 기존의 내장함수나 예약어를 사용하지 않게 하는 것!!

``` python
import keyword
print(keyword.kwlist) # 예약어 확인하는 법!
dir(__builtins__) # 내장함수 확인하는 법!
```



### 타입형 보기

* 8진수 : 0o, 2진수 : 0b, 16진수 0x # 여기서 대문자 소문자 상관 ㄴㄴ

``` python
a = 0xAD12 # 숫자에도 대문자, 소문자 상관없음 
print(a) # 44306
# 한 가지더 ! 0b 뒤에는 1과 0만 가능
# 그럼 8진수는? 알겟지?
```

* 오버플로우가 없다. (숫자가 범위를 넘어서면 메모리를 시스템적으로 더 가져옴!)
* 시스템적 int이 maxsize를 보고 싶다면

``` python
import sys
max_int = sys.maxsize
# sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
print(max_int)
super_max = sys.maxsize * sys.maxsize
print(super_max)
# -> print
# 2147483647
# 4611686014132420609
```

* 컴퓨터는 2진수 처리방식이라서 실수연산이 정확하지 않다.
* 그러므로 둘을 비교해주는 방식이 다른데

``` python
# 제일 잘 비교되는 것
import math
math.isclose(a, b)

# 부동소수점 연산 반올림, 추천 ㄴㄴ
import sys 
abs(a - b) <= sys.float_info.epsilon

# 기본적인 처리방법, 이거도 추천 ㄴㄴ
abs(a - b) <= 1e-10
```

* 문자열에서 복소수타입으로 변환가능

``` python
complex('1+2j') # 이렇게, 하지만 주의할 점! 중간에 공백(' ')이 들어간다면 오류남.
```

* 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`
* 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`



##### 이스케이프 시퀀스

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분합니다.

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|    \n    |      줄 바꿈      |
|    \t    |        탭         |
|    \r    |    캐리지리턴     |
|    \0    |     널(Null)      |
|    \\    |        `\`        |
|    \'    | 단일인용부호(`'`) |
|    \"    | 이중인용부호(`"`) |

``` python
name = 'Kim'

# 퍼센트 포멧팅
print('Hello, %s %s' %(name, name))
# 문자 포멧팅
print('Hello, {}, {}'.format(name, name)) # 이름 지정도 가능
# f 스트링
print(f'Hello, {name}')

# 포맷팅도 뒤에 연산 가능 및 소수점 선택 출력가능
pi = 3.13214123
print('Hello, {:.5}, {}'.format(pi, name))
# Hello, 3.1321, Kim

# f 스트링 연산 가능, 소수점 출력 가능
pi = 3.141592
f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2}'


```

``` python
#f스트링의 장점 및 datetime 보기. 근데 포멧팅에서도 가능
import datetime
today = datetime.datetime.now()
print(today)
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
```



* 비교연산자

  * `is`객체 아이덴티티
  * `is not`부정된 객체 아이덴티티

* divmod(a, b)

  ``` python
  quotient, remainder = divmod(5, 2) # 2개로 나옴
  ```



### 연산 주의할 점

* 우선순위 연산자 주의  - 밑에 순서
  1. `()`을 통한 grouping
  2. Slicing
  3. Indexing
  4. 제곱연산자 `**`
  5. 단항연산자 `+`, `-` (음수/양수 부호)
  6. 산술연산자 `*`, `/`, `%`
  7. 산술연산자 `+`, `-`
  8. 비교연산자, `in`, `is`
  9. `not`
  10. `and`
  11. `or`



* 단축 평가 주의
* in 연산자 bool로 평가.

``` python
# 파이썬에서 -5 부터 256 까지의 id는 동일합니다.
a = 3
b = 3
a is b # -> True


# 257 이루의 id 는 다릅니다.
a = 257
b = 257
a is b # False

# 이게 가능한 이유, 리스트에서도 주소는 16씩 움직이더라.
```



## jupyter 01

![image-20200809162201940](C:%5CUsers%5Cfksk9%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200809162201940.png)

+ immutable -> frozenset



## jupyter 02

#### `enumerate()`

인덱스(index)와 값(value)을 함께 활용 가능

> `enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있습니다.
>
> - `enumerate()`는 [내장 함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있습니다.

``` python
# 
classroom = ['Kim', 'Hong', 'Kang']
class_list = list(enumerate(classroom))
print(class_list)
print(type(class_list[0]))
# [(0, 'Kim'), (1, 'Hong'), (2, 'Kang')]
# <class 'tuple'>

classroom = ['Kim', 'Hong', 'Kang']
class_list = list(enumerate(classroom, start = 5))
print(class_list)
print(type(class_list[0]))
# [(5, 'Kim'), (6, 'Hong'), (7, 'Kang')]
# <class 'tuple'>
```



## jupyter 03

### 기본인자

``` python
# 기본인자는 함수 매개변수에 마지막에 넣어야 한다.
def greeting(age, name='john'):
    return f'{name}은 {age}살입니다.'
```

``` python
def greeting(age, name='john'):
    return f'{name}은 {age}살입니다.'

# 키워드 인자는 호출 순서를 바꿀 수 있다.
greeting(name='철수', age=24)
greeting(24, name='철수')
```

``` python
print('첫번째 문장')
print('두번째 문장', end='_')
print('세번째 문장', '네번째 문장')
print('다섯번째 문장', '마지막 문장', sep='/', end='끝!')
# 여러개 인자 처리. sep = '/' 이거 좀 제대로 알기.
'''
첫번째 문장
두번째 문장_세번째 문장 네번째 문장
다섯번째 문장/마지막 문장끝!
'''
```

* 가변인자 리스트

``` python
def my_fake_dict(**kwargs):
    return kwargs
# 가변인자 리스트
result = my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')

def my_func(*args):
    return args
# 가변인자 리스트
print(my_func(1, 2))
print(type(my_func(1, 2)))
```



## Jupyter 04

### 이름 검색 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

이것을, `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나갑니다.

- `L`ocal scope: 정의된 함수

- `E`nclosed scope: 상위 함수

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성



### 최대 깊이 재귀 및 재귀

* 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있다.

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용한다.
- 재귀 호출은 `변수 사용` 을 줄여줄 수 있다





## Jupyter 05

* error 종류

  ``` python
  try :
      # 코드실행
  except (ValueError, IndexError, ZeroDivisionError, Exception) as err:
      print (err)
      
  except #블라블라 :
  	# 여러개를 적을 때는 블라블라에 작은 범주부터 시작해야된다.
      # Exception은 모든 예외
  ```

* else, fianlly 실행?

  ``` python
  while True : # 이거랑 같이 잘씀
  	try :
      	# 할 코드
          break
  	except :
      	# 예외처리
          break
          
      # 밑의 두개는 둘 중 하나만 쓸 수 있다.
      
      else : # break 적용됨.
          print("break가 적용된다!")
          # try 후 실행되는 코드
      finally :
          print("break가 적용 안 된다!") # break 적용안됨
          # 뭐든 간에 무조건 마지막에 실행되는 코드.
  ```

* raise

  ``` python
  raise NameError('네임에러가 발생했습니다.') # 에러 강제 발생기
  ```

* asserts

  ``` python
  def my_div(num1, num2):
      result = num1 / num2
      
      # 앞의 식이 틀렸다면, err를 내준다. 뒤의 문자열을 출력하면서!
      # 식은 다른 걸로도 설정가능
      assert type(result) is int, '문자열을 입력하였습니다.'
      return result
  
      #assert type(num1) is int, '문자열을 입력하였습니다.'
      #assert type(num2) is int, '문자열을 입력하였습니다.'
  ```

  

## jupyter 06 ~ 07

### `'separator'.join(iterable)`

특정한 문자열로 만들어 반환합니다.

반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) 문자열로 반환합니다.

``` python
word = '안녕하세요'
words = ['안녕', 'hello']
'!'.join(word)
' '.join(words) # 여기서 요소가 int형이면 안됨.
# 안!녕!하!세!요!
# 안녕 hello
```



### `.lower()`, `.swapcase()`

``` python
a = 'hI! Everyone, I\'m kim'

# 바꾸기 및 밑으로 upper(),capitalize(),title() 도 가능
a.lower()
a.swapcase()
```



### list comprehension

``` python
# general list
even_list = [x for x in range(1, 11) if x % 2 == 0]
# pair list
pair = [(boy, girl) for boy in boys for girl in girls]
```



### zip, filter, map

``` python
# map
numbers = [1, 2, 3]

new_numbers = map(str, numbers)
print(new_numbers)
print(''.join(new_numbers))

# filter
def odd(n):
    return n % 2
new_numbers = list(filter(odd, numbers))
print(new_numbers)

# zip - 낮은 length의 list로 튜플을 만들어줌
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
pair = list(zip(girls, boys))
print(pair)
```

* Dictionary Comprehension

``` python
result = {key: '매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통' if value > 30 else '좋음' for key, value in dusts.items()}
```



## jupyter 08

``` python
# as 사용법!
from my_package.statistics.tools import standard_deviation as sd
sd([1,2,3,4,5])
```



## jupyter 09 ~ 11

> `type`: 공통 속성을 가진 객체들의 분류(class)

> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드
>
> - 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능하다.
> - `<클래스의 이름>`은 `PascalCase`로 정의한다.



### object 중심의 장점

**<wikipedia - 객체지향 프로그래밍>**

> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다.
>
> 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
>
> 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있다.

- 코드의 **직관성**
- 활용의 **용이성**
- 변경의 **유연성**



``` python
#
class MyClass:
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @staticmethod
    def static_method(arg):
        return arg
```