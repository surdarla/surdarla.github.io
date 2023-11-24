# 제어문

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Nov 23 Thu 17:10, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

제어문은 python을 다룰 때 기본적인 공부는 했기 떄문에, python javascript와 비교하는 형식으로 진행하고, 특이점이 있으면 admonition으로 표기한다.

## if

별다른게 없다. 그냥 javascript랑 거의 완전히 동일하다.

```java
boolean hasCard = true;
ArrayList<String> pocket = new ArrayList<String>();
pocket.add("papaer")
pocket.add("handphone")

if (pocket.contains("money")){
    System.out.println("택시타");
} else if (hasCard) {
    System.out.println("택시타");
} else {
    System.out.println("work")
}
```

## switch/case

if문과 비슷하지만 좀 더 일정한 형식이 있는 조건 판단문이다.

```java
public class Sample{
    public static void main(String[] args){
        int month = 8;
        String monthString = "";
        switch (month) {
            case 1: monthString = "Jan";
            break;
            case 2: monthString = "Feb";
            break;
            ...
            case 12: monthString = "Dec";
            break;
        }
        System.out.println(monthString);
    }
}
```

## for

```java
String[] numbers = {"one","two","three"};
for (int i = 0; i<numbers.length; i++){
    System.out.println(numbers[i]);
}
```

javascript할때 주구장창 봤던 구조이다.

for + if(continue)를 하면 조건반복문을 할 수 있다.

```java
public class LabelExam1{
    public static void main(String[] args){

    }
}
```

### 라벨 label

```{code-block} java labe
---
:name: java label
:caption: java for loop with label
:lineno-start: 1
---

outer: for (int i = 0; i < 5; i++) {
    inner: for (int j = 0; j < 5; j++) {
        if (j == 2) break outer; // 'outer' 라벨의 루프를 종료
        System.out.println("i = " + i + ", j = " + j);
    }
}
```

Java에서는 loop, block에 이름을 붙여서 사용하는 라벨이란 것이 있다. 이것은 중첩된 루프를 다룰 때 유용하다. 라벨을 사용하면 중첩된 루프 중 특정 루프로 직접 이동하거나, 그 루프를 종료할 수 있다. 이는 복잡한 루프 구조에서 특정 루프를 제어할 때 도움을 준다. 특이 중첩된 루프의 어떤 부분이 제어되고 있는지 명확하게 파악을 할 수 있어서 코드의 가독성의 측면에서도 좋다.

`break`
: 지정된 라벨이 붙은 루프를 종료

`continue`
: 지정된 라벨이 붙은 루프의 다음 반복으로 skip

라벨과 위의 두 개의 명령어를 사용해서 다중 반복문에서 연산을 명확하게 하는 것이 가능하다.

### for each

이 부분은 사실은 크게 다른 점이 없긴 하지만, javascript의 forEach와 다른 언어들을 비교하기 위해서 조금 정리를 해보았다. 크게 다른 점은 없지만 javascript에서는 당장에 요소와 반응해야하는 반응형 언어이기 때문에 요소에 바로 함수를 적용하는 모습을 보이고, 새로운 배열을 return 하는 것이 아니라 기존의 배열을 변경하는 모습을 보인다.

::::{grid} 1 2 2 3
:gutter: 2
:class-container: full-width

:::{grid-item-card} java

```java
for(String name : names) {
    System.out.println(name);
}
```

^^^

- Java에서 for-each 루프는 배열이나 컬렉션의 각 요소를 순회하기 위한 간단한 방법을 제공합니다.
- 이 루프는 내부적으로 Iterator를 사용하여 컬렉션의 요소를 순회합니다.
- 루프 변수는 읽기 전용이며, 컬렉션의 요소를 수정할 수는 없습니다.
+++
주로 읽기 전용
:::

:::{grid-item-card} JavaScript의 forEach() 메소드

```javascript
names.forEach(function(name) {
    console.log(name);
});
```

^^^

- JavaScript의 forEach() 메소드는 배열의 각 요소에 대해 지정된 함수를 실행합니다.
- forEach()는 배열의 각 요소에 대해 콜백 함수를 호출하며, 콜백 함수는 요소 값, 인덱스, 배열 자체를 인자로 받을 수 있습니다.
- 배열을 직접 변경할 수 있지만, forEach()는 새 배열을 반환하지 않습니다.
- 문법: `array.forEach(function(item, index, array) { ... });`
+++
- JavaScript의 forEach()는 콜백 함수를 사용하는 추가 유연성을 제공합니다.
- 원본 배열을 수정할 수 있습니다.
- javascript는 기본적으로 "지금" 함수의 행동 자체가 중요한 언어이다 보니 뭔가를 return하지 않고 function을 지금 수행하는 이런게 만들어 졋나 싶다.
:::

:::{grid-item-card} Python의 for 루프

```python
for name in names:
    print(name)
```

^^^

- Python의 for 루프는 시퀀스(리스트, 튜플, 문자열 등)를 순회하는 데 사용됩니다.
- Python의 루프는 간결하고 직관적이며, 루프 변수를 통해 각 요소에 접근할 수 있습니다.
- 루프 내에서 시퀀스의 요소를 수정하는 것이 가능하지만, 일반적으로 시퀀스 자체를 변경하는 것은 권장되지 않습니다.
+++
그냥 간결, 직관,, 그저 GOAT..
:::
::::
