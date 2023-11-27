# Java

```{figure} https://i.namu.wiki/i/zQ09oXQUxhmIJDQmQNV38Zr0_Mot9Ey-RF6fTTonYvyUYHHG-W0oDQ4cHUqfC1KVyuTiE3mOWYLnOi4n3LQ28qp1sWAq40oHOrae5PpHdn2knPQmaoXjv8RVXMteV_3WKKG8Ts893bAzcjlQqotQQA.svg
---
name : java_logo
align : center
width : 40 %
alt : java_logo
figclass : margin
---
제임스 고슬링이 만들었는데 자바 커피를 좋아해서 이름지었다고 한다.
```

## 언어 자체에 대한 정보

- 썬 마이크로즈 시스템즈에서 1995년 개발
- 현재는 오라클이 인수해서 Java의 저작권은 오라클에 있다.
- C#과 문법적 성향이 굉장히 비슷하다
- Java SE(Standard), Jakarta EE(Enterprise Server), Java ME(Embedded system)
- [OOP(객체 지향 프로그래밍 언어)](oop)
  - 객체 지향이긴 하나 원시 타입은 객체 취급 하지 않는다.
- 프로젝트 관리 도구
  - Maven(라이브러리 관리, 프로젝트 결과물 배포 관리 도구)
  - Gradle - 안드로이드 프로젝트 기본 프로젝트 관리 도구

### 프로그램 실행 순서

> JDK(java dev kit, ~.java) $\to$ javac(compiler, ~.class) $\to$ JVM(java vm) $\to$ cpu

- c는 기계어로 직접 컴파일 하지만, java는 바이트코드(.class)로 컴파일한다는 점이 다르다.
  - 플랫폼에 맞는 JVM만 설치하면 어디서든 같은 코드로 동작이 가능하다는 장점이 있다.
  - 해서 **플랫폼 독립적**이라고 한다.

- JVM은 클래스를 어디서 찾습니까?
  - CLASSPATH(현재는 .)에서 찾아서 .class 바이너리 파일을 실행시킨다.
  - 현재 경로라고 말하면 어지러워진다(면접끝)
  - 동일한 파일명을 가진 .class 바이트파일을 classpath에서 찾아서 읽어드린 클래스 정보를 heap에 올린다.
  - 인스턴스가 아니라는 점을 주의하자.
  - static method, instance method에 대한 정보를 이제 모두 안다.
  - 가장 먼저 main method를 찾고 실행한다.

## 코드 구조

```{code-block} java
:name: java_intro_code
:emphasize-lines: 2,5

/* 클래스 블록 */
public class 클래스명 {

    /* 메서드 블록 */
    [public|private|protected] [static] (리턴자료형|void) 메서드명1(입력자료형 매개변수, ...) {
        명령문(statement);
        ...
    }

    /* 메서드 블록 */
    [public|private|protected] [static] (리턴자료형|void) 메서드명2(입력자료형 매개변수, ...) {
        명령문(statement);
        ...
    }

    ...
}
```

### block

```{figure} https://wikidocs.net/images/page/278/02-1_statement.png
---
name : blocks
align : center
alt : block image
---
중괄호 `{}`로 둘러싸인 코드의 집합
```

1. 클래스 블럭
2. 메소드 블록(Method Blocks)
3. 조건문 블록(Conditional Blocks)
4. 반복문 블록(Loop Blocks)
5. 익명 블록(Anonymous block) - instance initialization block, static initial block

위와 같은 여러 블록이 java에서 존재한다. 블록은 코드의 구조, 조건 및 반복 제어, 변수의 범위 제한 등 여러 가지 역할을 하면서 범위를 규정하는 역할을 한다. 블록 내에서 선언된 변수는 그 블록 내애서만 유효한 블록 scope를 가지며, 블록 밖에서는 접근할 수 없다.

::::{grid} 3
:gutter: 1
:class-container: full-width

:::{grid-item-card} class block

```java
/* 클래스 블록 */
public class 클래스명 {
}
```

^^^
클래스의 이름은 Main이 일반적이지만 다른 것일 수도 있다. 하지만 클래스 이름은 파일의 이름과 같아야한다(className.java).
+++
public은 자바의 접근 제어자로, 어디서든 이 클래스에 접근할 수 있음을 말한다.
:::

:::{grid-item-card} method block

```java
    /* 메서드 블록 */
    [public|private|protected] [static] (리턴자료형|void) 메서드명1(입력자료형 매개변수, ...) {
        명령문(statement);
        ...
    }
```

^^^
클래스 블럭 안에 highlight된 부분이 method block 이다.
+++
main method가 해당 클래스 프로그램의 시작점이 된다.
:::

:::{grid-item-card} statement

```java
명령문(statement);
```

^^^
메서드 블럭 안에 이제 `Statement 명령문` 이 있다. 이제 실제로 컴퓨터가 동작해야하는 부분에 대한 규정이 들어가 있다.
+++
`;`가 문장이 끝난 것임은 javascript와 비슷하다.
:::

::::

% definition list
public|default|private|protected
: 접근제어자(access modifier), private $\to$ defautl $\to$ protected $\to$ public 순으로 접근가능 범위가 넓어진다.

- `private` : 해당 클래스 안에서만 접근 가능
- `default` : 별도 지정안되면 이거다. 동일한 package(folder) 안에서만 접근 가능
- `protected` : 동일 package의 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근 가능
- `public` : 어떤 클래스에서도 접근 가능

static method
: 아무것도 없으면 instance initialization block이며, 이럴 경우에는 instance를 만들 때마다 실행된다. 즉 instance마다 초기화 값을 다르게 만들어주고 싶을때 사용하면 된다.\
반면 static일 경우에는 static initial block이라고 해서 클래스가 처음 JVM에 로드될 때 한 번만 실행된다. 주로 클래스 변수 초기화에 사용된다. 모든 instance가 같은 값으로 초기화되기를 원할 때 사용한다. 진정한 초기화 느낌스? 인스턴스 생성없이 실행될 수 있으며 그 이유는 static을 사용한 변수는 클래스가 메모리에 올라갈 때 자동으로 하나 생성되기 때문이다.

```{admonition} Heap memory
:class : note, margin

여기서 메모리라고 하는 부분은 [heap](heap)을 말한다. heap은 자료구조의 하나로써 max,min을 찾아내는 연산을 빠르게 하기 한 완전 이진트리를 말한다. 일정한 특징을 가지는 구조의 자료를 말하는 것이다. 파이썬의 heapq는 이러한 특징을 built-in으로 구현해 놓은 것이다.
```

```{admonition} class.static
:class : caution,

static method는 클래스 명 다음에 사용해준다. 이게 프로그래머 간의 관례이며, 가독성이 높고 코드유지보수에도 도움이 된다. 참조변수.static 이런 식으로 사용하진 말라는 이야기이다.
```

(리턴자료형|void)
: 메서드의 리턴 자료형을 규정하는 부분이다. void일 경우는 리턴값이 없음을 의미한다. null도 아니라 아예 반환하는게 없기 때문에 변수에 할당하려면 compile error가 발생한다.

메서드명1(입력자료형 매개변수, ...)
: 여기서 부터 프로그램이 시작된다. 그래서 프로그램 시작점이라고 불린다. `String[] args` : str list가 변수로 들어와야 하고 밑에서는 args로 사용한다. 자료형 + 변수명

- 클래스는 필드와 메소드를 가질 수 있다.
  - `System.out.println` : 마치 자동차.엔진.시동해 처럼 `class.field.method`
  - 그리고 이 긴 것을 명령문(statement)라고 한다.

## Field

- 클래스가 가지는 속성을 java에서 Field라고 말한다.
- 다른 언어에서는 멤버변수라고 말하기도 한다.
- 필드는 어떤 키워드와 함께 사용하느냐에 따라서 사용방법이 달라진다.
- 종류
  - Class Field : static
  - Instance Field : ❌ static
- 필드는 첫번째 글짜는 소문자로 시작하는 것이 관례이다.

```zsh
[접근제한자 : public|default|private|protected] [static] [final] type fieldName [=default_value|false|null];
```




## 앞으로 진행될 내용

```{tableofcontents}
```

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
