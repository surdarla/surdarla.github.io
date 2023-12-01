(oop)=
# 객체 지향 프로그래밍

::::{div} sd-rounded-3 sd-border-2 sd-shadow-md sd-p-5 sd-m-5
객체지향의 핵심은 "메시징"이다. 훌륭하고 성장 가능한 시스템을 만들기 위한 핵심은 모듈 내부의 속성과 행동이 어떤가보다 모듈이 어떻게 커뮤니케이션하는가에 달려있다.
:::{div} sd-text-right sd-text-muted
-- Alan Curtis Kay
:::
::::

객체와 객체는 관계가 존재한다. 관계는 곧 커뮤니케이션이다. 객체간에 메소드를 호출하는 것을 메시징이라고 말한다. 메소드가 언제 어떻게 호출되는지가 객체 지향 프로그래밍의 핵심이라고 말할 수 있다.

## 객체는 자율적임 책임을 진다

::::{div} sd-rounded-3 sd-border-2 sd-shadow-md sd-p-5 sd-m-5

자율적인 객체란 스스로 정한 원칙에 따라 판단하고 스스로의 의지를 기반으로 행동하는 객체다. 객체가 어떤 행동을 하는 유일한 이유는 다른 객체로부터 요청을 수신했기 때문이다. 요청을 처리하기 위해 객체가 수행하는 행동을 책임이라고 한다.

자율적인 책임의 특징은 객체가 어떻게 해야하는가가 아니라 **무엇을 해야하는가**를 설명한다는 것이다.

:::{div} sd-text-right sd-text-muted
-- 객체지향의 사실과 오해(조영호)
:::
::::

- 책임 : response, 반응, resposible?. 자판기에 동전 넣으면 나올 것이 나와줘야한다.
- 메시징 : 객체가 다른 객체에 메소드를 호출하는 것, method call

## 캡슐화

encapsulation 캡슐화는 관련된 것을 모아서 가지고 있는 것을 말한다. 관련된 것을 잘 모을수록 정보의 응집도(Cohesion)이 높다고 표현한다. 좋은 객체는 **응집도는 높고 (객체와 객체간에는)결합도(coupling)은 낮다**. 물건을 사용하기 편하려면 결합도가 낮아야한다.

## 다형성

**Polymorphism**은 해당 프로그래밍 언어의 자료형 체계의 성질을 나타내는 것이다. 프로그램 언어의 각 요소(constant, variable, funtion, object, method)이 다양한 자료형(type)에 속하는 것이 허가되는 성질을 가리킨다. 반댓말은 단형성으로, 프로그램 언어의 각 요소가 한 가지 형태만 가지는 성질을 가리킨다.

### method overloading

다형성에 대한 설명이 한국말인데 겁나게 어렵다. 다형성을 활용한 방법 중의 하나인 method overloading의 예시를 직접 확인해보면 조금 이해하기 쉬울 것이다. `System.out.println()`을 보자. 여기 안에 들어갈 수 있는 인자는 int, float, double, String 등이 될 수 있다. 중요한건 메소드는 인자에 변화하지 않고 출력이라는 기능을 사용할 때는 전부 동일하게 사용한다. 이름을 잘 지은 것이다. printIntln, printFloatln 등으로 변수에 따라 전부 다른 메소드를 사용한다면 외워야할 것이 몇 배는 늘어날 것이다.

메서드의 이름은 같고 매개변수의 갯수나 타입이 다른 함수를 정의하는 것을 말한다. 리턴값만을 다르게 갖는 오버로딩은 작성할 수 없다.

> 요지는 내가 힘들게 만들어서 사용하는 사람은 쉽게 사용하도록 만드는 과정이다.

### method overriding

부모 클래스의 메서드를 자식 클래스가 재정의하는 것을 말한다. 메서드의 이름은 물로 파라미터의 갯수나 타입도 동일해야 하며, 주로 상위 클래스의 동작을 상속받은 하위 클래스에서 변경하기 위해서 사용된다. 기억해야할 것은 **메서드가 오버라이딩 되면 무조건 자식의 메서드가 실행된다.** 참조 타입이 부모 타입이라고 하더라도 실제 동작은 인스턴스에서 오버라이딩 된 기능이 동작하는 것이다. 자식이기는 부모 없다

```java
Car car = new Bus();
car.run(); 
```

car도 `public void run()` 메서드를 가지고 있고, bus도 `public void run()` 메서드를 가지고 있다면 $\to$ bus의 run() 메서드가 실행된다.

```java
Car c1 = new Bus();
Bus b2 = (Bus)c1;

Car c2 = new 이층버스();

```

이렇게 되면 c1이 참조하는 Bus instance를 Bus 타입으로 변환해서 b2가 참조하게 하라는 의미이다. 자식 인스턴스를 부모 타입의 참조 변수로 참조하는 것은 당연하게 가능하다. 버스를 상속받고 있는 이층 버스가 있다고 생각해보자. "이층버스는 자동차다". 이것은 말이 되지만, 모든 자동차는 이층버스라고 하는 것은 틀린 말이 된다.

### field overriding

::::{grid} 1 1 2 3
:gutter: 3
:class-container: full-width

:::{grid-item-card}
```{code-block} java
:caption: Parent.java
:emphasize-lines: 2
:lineno-start: 1

public class Parent {
    public int i = 5;
    public void printI(){
        System.out.println("parent - printI() : " + i);
    }
}
```
:::

:::{grid-item-card}
```{code-block} java
:caption: Child.java
:emphasize-lines: 2
:lineno-start: 1

public class Child extends Parent{
    public int i = 15;
    public void printI(){
        System.out.println("child - printI() : " + i);
    }
}
```
:::

:::{grid-item-card}

```{code-block} java
:caption: Exam01
:emphasize-lines: 10,11
:lineno-start: 1

public class Exam01{
    public static void main(String[] args){
        Parent p1 = new Parent();
        System.out.println(p1.i);
        p1.printI();

        Child c1 = new Child();
        System.out.println(c1.i);
        c1.printI;

        Parent p2 = new Child(); // child는 parent의 자식
        System.out.print(p2.i); // 5
        p2.printI(); // 15
    }
}
```
:::
::::
필드는 type을 따라가고 메소드는 오버라이딩 된 자식의 메소드가 실행된다. 마지막 두 줄이 주요한데, p2.i = 5, p2.printI() = 15의 결과가 나온다. 메소드는 오버라이딩 되면 무조건 자식의 것을 실행한다고 위에서 암기했었다. 부모의 필드값(i)은 현재 5이다. 그래서 필드를 그냥 실행(p2.i)을 하면 5가 나온다.

하지만 method를 실행하면(p2.printI()) 15가 나온다. 필드가 오버라이딩 되서 자식의 값이 사용되다면 부모 클래스를 만든 사람이 예상하지 못한 결과가 출력될 것이기 때문이다. 그렇기 때문에 필드는 부모 타입을 따라간다.

method overriding만 기억을 하면 된다. 이는 정보 은닉(information hiding)이라는 객체 지향의 중요한 특징이기 때문이다. **필드는 직접 접근하는 코드는 사용하면 안된다.** 메서드를 통해서만 필드값을 사용해야한다. 접근지정자를 사용해서 은닉하게 된다.