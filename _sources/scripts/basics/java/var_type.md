# 변수와 자료형

## 변수 variable

변수란 하나의 값을 저장하기 위한 메모리 공간을 말한다. 변수는 자료형을 어떤 것을 사용하느냐에 따라서 필요한 메모리 공간(bit)가 달라짐으로 필요에 따라 그 자료형을 맞게 사용해줘야한다.

## 자료형 type

아래의 자료형들은 원시형(primitive) 자료형이다. 이러한 원시 자료형은 new 키워드로 값을 생성할 수 없다. 오직 literal 표기 방식으로만 생성이 가능하다. 특이한 것은 String은 리터럴 표기 방식으로 표기할 수 있지만 원시 자료형에는 포함되지 않는다. 특별우대 해주는 자료형이기 때문에 원시 자료형이라고 착각하면 안된다. 원시 자료형은 char이다.

| 자료형  | 카테고리 | 크기 (비트) | 최소값                     | 최대값                    | 기본값   |
| :------ | :------- | :---------- | :------------------------- | :------------------------ | :------- |
| byte    | 정수형   | 8           | -128                       | 127                       | 0        |
| short   | 정수형   | 16          | -32,768                    | 32,767                    | 0        |
| int     | 정수형   | 32          | -2,147,483,648             | 2,147,483,647             | 0        |
| long    | 정수형   | 64          | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 | 0L       |
| float   | 실수형   | 32          | 1.4E-45                    | 3.4028235E38              | 0.0f     |
| double  | 실수형   | 64          | 4.9E-324                   | 1.7976931348623157E308    | 0.0d     |
| char    | 문자형   | 16          | '\u0000' (0)               | '\uffff' (65,535)         | '\u0000' |
| boolean | 불리언형 | -           | -                          | -                         | false    |

```{admonition} String은 뭐노?
:class : attention,  
`String`은 기본 자료형이 아니라, 참조 자료형(Reference type)이다. 내부적으로 문자의 배열로 구현되어 있다. 불변성, 클래스(`java.lang.String`)에 의해 제공된다.
```

### 1. char

::::{grid} 2
:gutter: 1
:class-container: full-width

:::{grid-item-card} object
```java
String a = new String("something")
```
^^^
이렇게 `new`를 사용하는 방식은 항상 새로운 String object를 만든다. 객체를 만드는 것은 메모리를 차지하고, 자체가 새로 상성된 자료형과 같은 것이다. 컴파일 최적화에도 도움이 되지 않는다.
+++
이러한 방식보다는 ...
:::

:::{grid-item-card} literal
```java
String a = "something"
```
^^^
앞과 다르게 객체를 생성하지 않고 문자열을 그대로 넣는 방식을 `literal`이라고 한다. 이러한 방식은 가독성도 높고, compile 최적화에도 도움이 된다.
+++
왠만하면 문자열 선언은 이러한 방식으로 하자.
:::
::::

#### char 내장 메서드

`new`
: 객체를 만들 때 사용

`equals`
: 문자열의 값을 비교할 때. type비교도 아니고 "==" 와 같은 논리연산도 아니다. value만 비교한다.

`indexOf(str)`
: 문자열에서 특정 문자가 시작되는 위치,index return

`substring(start, end)`
: 문자열에서 특정 부분을 뽑아내기. 해당 args로 위치 특정

`replaceAll(str, substitute str)`
: 문자열에서 특정 문자열 대체 문자로 바꾸기. 근데 나오는 것마다 모두

`toUpperCase`, `toLowerCase`
: 설명안함.

`String.format("... %d ...")`
: 파이썬 f-string처럼 이용하는 것이다.   

| 코드 | 설명                     |
| :--- | :----------------------- |
| %s   | 문자열(String)           |
| %c   | 문자 1개(character)      |
| %d   | 정수(Integer)            |
| %f   | 부동소수(floating-point) |
| %o   | 8진수                    |
| %x   | 16진수                   |
| %%   | Literal % (문자 % 자체)  |

좋은 것은 %s를 사용하면 자동으로 파라미터 값을 문자열로 바꾸어 사용해서 편하다.

### 2. number

- 정수(int, long), 실수(float, double) 4가지가 있다.
- 기본형은 32bit이고 긴 것은 이의 두 배인 64bit이다.


## naming rule

클래스 이름
: 클래스 명은 명사로 한다.\
대문자로 시작한다(javascript는 소문자로 시작하는 것과는 다르다).\
이 다른 것을 `pascal case`라고 한다.

메서드 이름
: 메서드 명은 동사로 한다.\
소문자로 시작한다.\
javascript처럼 하는 것을 `camel case`라고 한다.

변수 이름
: 변수는 숫자로 시작할 수 없다.\
_, $ 만 사용가능\
int, class, return 과 같은 built-in keyword는 변수명으로 사용 불가

## referance

- [wikidocs java](https://wikidocs.net/1936)

```{raw} html
<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="surdarla/surdarla.github.io"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
```
