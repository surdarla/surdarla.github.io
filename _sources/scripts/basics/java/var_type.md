# 변수와 자료형

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Nov 23 Thu 13:17, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

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
: 파이썬 f-string처럼 이용하는 것이다. 좋은 것은 %s를 사용하면 자동으로 파라미터 값을 문자열로 바꾸어 사용해서 편하다.

:::{table} String.format 정리
:width: 60%
:align: center

| 코드 | 설명                     |
| :--- | :----------------------- |
| %s   | 문자열(String)           |
| %c   | 문자 1개(character)      |
| %d   | 정수(Integer)            |
| %f   | 부동소수(floating-point) |
| %o   | 8진수                    |
| %x   | 16진수                   |
| %%   | Literal % (문자 % 자체)  |

:::

### 1-1. StringBuffer

StringBuffer는 문자열을 추가하거나 변경할 때 주로 사용하는 자료형이다. String을 사용하면 객체를 하나 만드는 것이다. 하나의 String에 추가나거나 하려면 다른 하나를 또 만들고 그 뒤에 붙이던가 해야한다. 하지만 StringBuffer는 그럴 필요가 없다. 객체를 하나만 만들고 가지고 놀면된다. 물론 그만큼 기본 String에 비해서 무거운 자료형이다. 때문에 경우에 잘 맞게 사용하는 버릇을 들이자.

### 2. number

- 정수(int, long), 실수(float, double) 4가지가 있다.
- 기본형은 32bit이고 긴 것은 이의 두 배인 64bit이다.

### 3. Array

다른 언어들과 마찬가지로 `[]`로 하되, `int[] array_name = {1,2,3,4}`, `String[] array_name =- {'a','b'...}` 이런 식으로 표현한다.

- **고정된 크기** : `String[] array_name = new String[7]` 이런 식으로 배열의 길이를 먼저 정할 수 있다.
- **인덱스 접근** : index로 접근하는 방식은 동일하다 `array_name[1]`
- **배열의 크기** : 배열의 길이를 구하는 방식은 javascript와 비슷하다. `array_name.length` -- 이거가 주의해야 할 것이 배열말고 list, map 같은 다른 경우들은 `size()`로 구하는 차이가 있다.
- python의 IndexError는 자바에서는 `ArrayIndexOutOfBoundsException`으로 표기된다.

### 4. List

우리가 맨날 python의 list는 사실 이것이다. 배열이지만 **배열의 크기가 지정되어 있지 않은** 특징을 가지는 배열을 말한다.

::::{grid} 2
:gutter: 2
:class-container: full-width

:::{grid-item-card} Java의 List 인터페이스
:link: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        fruits.remove("Banana");

    }
}
```

^^^

- List는 Java 컬렉션 프레임워크의 일부입니다.
- 크기가 동적으로 변할 수 있는 배열과 같은 객체의 집합을 나타냅니다.
- Java의 List는 제네릭을 사용하여 다양한 타입의 객체를 저장할 수 있습니다.
- 주로 ArrayList, LinkedList 등의 구현 클래스를 통해 사용됩니다.
- 타입 안정성이 보장되며, 컴파일 시간에 타입 체크가 이루어집니다.
+++
`import java.util.ArrayList`는 package를 현재 코드에서 사용하기 위한 선언문이다. Java.util은 기본 패키지이다.
:::

:::{grid-item-card} Python의 리스트
:link: https://docs.python.org/3/library/stdtypes.html?highlight=list#list

```python
fruits = ["Apple", "Banana", "Cherry"]

fruits.remove("Banana")

```

^^^

- Python의 내장 데이터 타입 중 하나입니다.
- 여러 다른 타입의 요소를 단일 리스트에 저장할 수 있습니다.
- 동적 배열 구현으로, 크기가 자동으로 조정됩니다.
- 내장된 다양한 메소드를 통해 리스트를 쉽게 조작할 수 있습니다.
- 타입이 동적이며, 런타임에 타입이 결정됩니다.
:::

::::

:::{table} java_list vs python_list
:width: 80%
:align: center

| 기능                    | Java (List 인터페이스)                 | Python (리스트)       |
| :---------------------- | :------------------------------------- | :-------------------- |
| 요소 추가               | `add(element)`                         | `append(element)`     |
| 특정 인덱스에 요소 추가 | `add(index, element)`                  | -                     |
| 요소 제거               | `remove(element)`                      | `remove(element)`     |
| 인덱스로 요소 제거      | `remove(index)`                        | `pop(index)`          |
| 리스트 크기             | `size()`                               | `len(list)`           |
| 특정 요소 검색          | `get(index)`                           | `list[index]`         |
| 요소 존재 여부 확인     | `contains(element)`                    | `element in list`     |
| 리스트 비우기           | `clear()`                              | `clear()`             |
| 특정 인덱스의 요소 변경 | `set(index, element)`                  | `list[index] = value` |
| 리스트 복사             | `new ArrayList<>(list)`                | `list.copy()`         |
| 리스트 정렬             | `list.sort(Comparator.naturalOrder())` | list.sort             |
:::

### 5. Map

Map은 python 딕셔너리랑 비슷한 것이라고 보면 된다. `key-value` pair로 구성된다. 다른 언어를 통합해서 보면 [hash, associate array](hash)이다. 배열처럼 index로 순차적으로 찾는 것이 아니라, key를 이용해서 한 번에 value값에 접근할 수 있는 장점이 있다. 이것이 곧 hash의 장점이기도 하다.

기본적으로 `import java.util.~Map` 식으로 패키지를 가져와야하고, HashMap, LinkedHashMap, TreeMap등이 있다.

::::{grid} 2
:gutter: 2
:class-container: full-width

:::{grid-item-card} Java의 Map
:columns: 6

```java
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> ageMap = new HashMap<>();

        ageMap.put("Alice", 30);
        ageMap.put("Bob", 25);
        ageMap.put("Charlie", 35);

      //   System.out.println("Bob's age: " + ageMap.get("Bob")); // Bob의 나이 출력

        ageMap.remove("Charlie"); // Charlie 항목 삭제

        for (Map.Entry<String, Integer> entry : ageMap.entrySet()) {
            // System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

^^^

- Map은 인터페이스이며, HashMap, TreeMap, LinkedHashMap 등 다양한 구현을 가지고 있습니다.
- Map은 키와 값을 Object 타입으로 저장합니다. 따라서 모든 종류의 객체를 키 또는 값으로 사용할 수 있습니다.
- 키는 고유해야 하며, 각 키는 하나의 값을 매핑합니다.
+++
- Java에서는 사용자 정의 객체를 키로 사용할 때 hashCode()와 equals() 메소드를 적절히 오버라이드해야 합니다. 이는 객체의 해시 코드를 생성하고 객체의 동등성을 비교하는 데 사용됩니다.
- Java의 HashMap은 순서를 유지하지 않습니다. 순서가 중요한 경우 Java에서는 LinkedHashMap을 사용할 수 있습니다.
:::

:::{grid-item-card} Python의 dict
:columns: 6

```python
age_map = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

# print(f"Bob's age: {age_map['Bob']}") # Bob의 나이 출력

del age_map["Charlie"] # Charlie 항목 삭제

# for name, age in age_map.items():
#     print(f"{name}: {age}")
```

^^^

- Python의 딕셔너리는 내장 타입으로, 해시 테이블을 기반으로 구현되어 있습니다.
- 키는 불변(immutable) 타입이어야 하며, 여러 타입의 값을 저장할 수 있습니다.
- Python 3.7+부터는 딕셔너리가 삽입 순서를 유지합니다.
+++
Python에서는 키로 사용되는 객체가 불변(immutable)이어야 하며, 내부적으로 `__hash__()`와 `__eq__()`메소드를 사용하여 해시 코드를 생성하고 동등성을 비교합니다. Python 딕셔너리는 삽입 순서를 유지
:::
::::

:::{table} Java Map vs Python dict
:width: 80%
:align: center

| 기능              | Java (Map)             | Python (dict)            |
| :---------------- | :--------------------- | :----------------------- |
| 요소 추가         | `put(key, value)`      | `dict[key] = value`      |
| 요소 접근         | `get(key)`             | `dict[key]`              |
| 요소 제거         | `remove(key)`          | `del dict[key]`          |
| 크기 확인         | `size()`               | `len(dict)`              |
| 키 존재 여부      | `containsKey(key)`     | `key in dict`            |
| 값 존재 여부      | `containsValue(value)` | `value in dict.values()` |
| 키 목록 가져오기  | `keySet()`             | `dict.keys()`            |
| 값 목록 가져오기  | `values()`             | `dict.values()`          |
| 키-값 쌍 가져오기 | `entrySet()`           | `dict.items()`           |
| 모든 요소 제거    | `clear()`              | `dict.clear()`           |
:::

## static

public static void classname() 뭐 이런 식으로 해당 클래스의 메인 메소드를 많이 만들어서 사용하곤 하는데 여기서 static이 무슨 의미인지를 알아야한다. static method는 인스턴스를 생성하지 않아도 메모리에 올라가 있다는 것을 말한다. 프로그래밍에 있어서 사용가능 하다는 것은 메모리에 올라가 있다는 것을 의미한다. 폰노이만의 프로그램 내장방식이란 모든 프로그램은 메모리에 올라가야지만 실행될 수 있다는 개념을 말한다. 보통은 new연산자를 사용하면 메모리에 올라가서 인스턴스화 되고 이를 객체 혹은 인스턴스라고 부른다. static은 인스턴스화 하지 않아도 사용가능하다는 의미가 위의 개념들을 합치면 조금 더 이해하기 편할 것이다.

인스턴스를 만드는 3가지 방법
:  1. new 연산자와 생성자를 이용하여 만들기\ 2. 클래스 로더를 이용하여 만드는 방법\ 3. 메모리에 있는 인스턴스를 복제하여 만드는 방법

## 디자인 패턴

객체 지향 프로그램이라는 것은 객체를 만드는 방법을 고민하는게 아니라 객체 그 자체에 대해서 고민해야한다.

인스턴스 생성 방법
: 필요한 개수만큼 만들어야 한다.



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
