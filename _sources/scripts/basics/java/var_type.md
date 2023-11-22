# 변수 variable

변수란 하나의 값을 저장하기 위한 메모리 공간을 말한다. 변수는 자료형을 어떤 것을 사용하느냐에 따라서 필요한 메모리 공간(bit)가 달라짐으로 필요에 따라 그 자료형을 맞게 사용해줘야한다.



# 자료형 type

| 자료형  | 카테고리 | 크기 (비트) | 최소값                     |          최대값           |  기본값  |
| :-----: | :------: | :---------: | :------------------------- | :-----------------------: | :------: |
|  byte   |  정수형  |      8      | -128                       |            127            |    0     |
|  short  |  정수형  |     16      | -32,768                    |          32,767           |    0     |
|   int   |  정수형  |     32      | -2,147,483,648             |       2,147,483,647       |    0     |
|  long   |  정수형  |     64      | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 |    0L    |
|  float  |  실수형  |     32      | 1.4E-45                    |       3.4028235E38        |   0.0f   |
| double  |  실수형  |     64      | 4.9E-324                   |  1.7976931348623157E308   |   0.0d   |
|  char   |  문자형  |     16      | '\u0000' (0)               |     '\uffff' (65,535)     | '\u0000' |
| boolean | 불리언형 |      -      | -                          |             -             |  false   |

`String`은 기본 자료형이 아니라, 참조 자료형(Reference type)이다. 내부적으로 문자의 배열로 구현되어 있다. 불변성, 클래스(`java.lang.String`)에 의해 제공된다. 

# naming rul

클래스 이름
: |
클래스 명은 명사로 한다.
대문자로 시작한다(javascript는 소문자로 시작하는 것과는 다르다).
이 다른 것을 `pascal case`라고 한다.

메서드 이름
: |
메서드 명은 동사로 한다.
소문자로 시작한다.
javascript처럼 하는 것을 `camel case`라고 한다.

변수 이름
: |
변수는 숫자로 시작할 수 없다.
_, $ 만 사용가능
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
