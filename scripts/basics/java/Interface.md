# Interface

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Dec 04 Mon 17:45, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

"무슨 기능을 만들어야할까?" vs "구현부터 하기" 둘 중에서 뭐가 더 중요하다고 할 수 있을까? 어떤 기능을 만들어야할지 부터 고민해줘야한다. 인터페이스는 이러한 고민을 러프하게 먼저 만드는 툴과 같은 것이다. 만들어야할 기능들을 관련된 것 끼리 묶은 후 이름을 지어준다. 기본적으로는 아래와 같이 만들어주고 규칙이 존재한다.

```java
[public] interface InterfaceName {
  ....
}
```

- Upper CamelCase : 첫글짜대문자 로 이름을 지어줘야한다.
- interface 도 확장자가 `.java` 파일로 작성한다.
- interface의 모든 필드는 `public static final`이어야 하고, 모든 메소드는 public abstract이어야 한다.(~java7) `final, abstract`를 생략하면 자동으로 붙는다.
- Java 8 부터는 `default method`와 `static method`도 선언이 가능하다.

## LottoMachine 만들기

```java
//LottoMachine

package com.example;

public interface LottoMachine{
  int MAX_BALL_COUNT = 45;
  int RETURN_BALL_COUNT = 6;
  public void setBalls(Ball[] balls); //1. 1-45까지 씌여있는 balls 로또 기계에 넣는다
  public void mix(); //2. 섞는다.
  public Ball[] getBalls(); // 3. 섞인 balls 중 6개 pick
}
```

```java
package com.example

public class LottoMachineImpl implements LottoMachine{
  private Ball[] balls;

  @Override
  public void setBalls(Ball[] balls){
    this.balls = balls;
  }

//Math.random() ===> 0.0<= x < 1.0 실수값이 나온다.
  @Override
  public void mix(){
    for (int i = 0; i < 10000; i++){
      int x1 = (int)(Math.random() * LottoMachine.MAX_BALL_COUNT);
      int x2 = (int)(Math.random() * LottoMachine.MAX_BALL_COUNT);
      if (x1 != x2){
        Ball temp = balls[x1]; // 값치환 : type의 임시변수 필요. 백업
        balls[x1] = balls[x2];
        balls[x2] = temp;
      }//if
    }//for
  }

  @Override
  public Ball[] getBalls(){
    Ball[] result = new Ball[LottoMachine.RETURN_BALL_COUNT];
    for (int i = 0; i < LottoMachine.RETURN_BALL_COUNT; i++){
      result[i] = balls[i];
    }//for
    return result;
  }
}

```

```java
public class LottoMachineMain{
  public static void main(String[] args){

    Ball[] balls = new Ball[LottoMachine.MAX_BALL_COUNT];
    for (int i = 0; i < LottoMachine.MAX_BALL_COUNT; i++){
      balls[i] = new Ball(i+1);
    }

    LottoMachine lottoMachine = new LottoMachineImpl();
    lottoMachine.setBalls(balls);
    lottoMachine.mix();
    Ball[] result = lottoMachine.getBalls();

    for (int i = 0; i < result.length; i++){
      System.out.println(result[i].getNumber());
    }
  }
}
```

```java
public class Ball{
  private int number;
  public Ball(int number){ //불변
    this.number = number
  }
  public int getNumber(){
    return number;
  }
}
```

1. 어차피 인터페이스가 가지는 메소드들은 전부 추상클래스이기 때문에 `abstract`를 생략해도 상관이 없다.
2. `public static`도 필드에서 생략해도된다. 메모리에 인스턴스를 만들지 않아도 올라간다.
3. `new` 이런식으로 새로운 인스턴스 만들때 사용은 불가능하다.

### default method

interface 내부에 기본적으로 구현을 해놓아서 compile error, 실행 error가 안나도록 하는 것이다. java8부터 추가되었다. 여러 사용자들이 해당 인터페이스를 이용해 구현을 해버렸을때, 미리 구현된 것을 method를 제공함으로써 버전업을 해도 자식은 자식대로 실행되고 부모를 받아와도 다르지 않도록 하는 것이다.

## 팩토리 메소드 패턴

객체가 생성되는 과정을 숨겨주고, 완성된 인스턴스만 반환해주는 패턴을 말한다. 빈펙토리는 singleton pattern으로 객체를 만들었다.

```java
public class BeanFactory{
    private static BeanFactory instance = new BeanFactory();
    private BeanFactory(){
    }
    public static BeanFactory getInstance(){
        return instance;
    }

    public Bus getBus(){
        return new Bus();
    }
}
```

객체 생성에 있어서 Bus b1 = b2.getBus(); 이런식으로 아주 가능하다.

### 클래스 로더

```java
Class clazz = Class.forName("class full name");
Object obj = clazz.newInstance();
```

1. a() 메소드를 가지고 있는 클래스가 있다.
2. 이 클래스 이름이 아직 무엇인지 모르겠다
3. 나중에 이 클래스 이름을 알려주겠다.
4. a() 메소드를 실행할 수 있도록 코드 작성해라.

referenceVariable.a(); 이런식으로 해야 사용이 가능한데 이 변수명이 없이 어케 선언을 하노?! 이런 난감한 경우에 사용하는 것이다.

JVM은 class를 `classpath`에서 찾는다. 이름(className)에 해당하는 클래스 정보를 path에서 읽어서 그 정보를 clazz가 참조하도록 하는 과정이다.

```java
public class ClassLoaderMain{
    public static void main(String[] args) throws Exception{
        String className = "";
        Class clazz = Class.forName(className);
        Method[] getDeclaredMethods = clazz.getDeclaredMethods();
        for (Method m : declaredMethods){ //forEach문
            System.out.println(m.getName());
        }//for

        Object o = clazz.newInstance(); //instance 생성
        Method m = clazz.getDeclaredMethod("a",null);
        m.invoke(o, ...args:null) // object o 가 참조하는 객체의 m 메서드 실행
    }//main
}
```

사실 위의 과정은 `Obejct o = new Bus();`이거를 좀 풀어쓴거랑 비슷하다고 볼 수 있다. object는 쌉 조상님 타입이다. 또 이거랑 같은 것은 Bus b = (Bus)o; b.a(); 해보면 a가 나온다.

문자열로된 클래스 이름과 메서드만 있어도 표현이 가능하다는 것을 알려주기 위해서 위의 과정을 한 것이라고 한다. spring을 나중에 할 때 내부적으로 사용하고 있기 때문에 어렵지만 이해를 하고 넘어가는 것이 필요할 것으로 보인다.
