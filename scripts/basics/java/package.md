# package

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Nov 29 Wed 16:51, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

package는 아키텍쳐 정의에 따라서 정의 된다. 그리고 아키텍쳐에 맞게 패키지의 이름이 정의된다. 자바 기본을 공부할 떄는 아키텍쳐가 정의되어 있지 않기 때문에 암기 과목처럼 공부하게 된다.

패키지 이름을 짓는 법은

- 도메인을 거꾸로 적는다.
  - 그럼 com - example - project 순으로 파일이 생긴다. 이렇게 관리하기 쉽게 하려고 이런식으로 하는 것으로 보인다.
  - 같은 이름의 파일이 있으면 안되니깐 큰 규모에서 아래의 규모로 폴더를 구조화하고 같은 이름의 파일을 방지하기 위해서 이렇게 한 것으로 보인다.
  - import로 어디서 불러올지를 명확하게 선언하는 부분이 맨 위의 부분이라고 볼 수 있다.

## 상속

~는 ~의 종류다. 라는 말처럼 말이 되어야한다. "~ is a ~", ~ is kind of ~" 이런 식으로 표현할 수 있어야한다. **일반화**시키는 것이다. tv도 전자레인지도 다 전자제품의 하나로 볼 수 있다.

상속은 위에서 본 것 처럼 일반화와 확정이라는 개념을 합한 것이라고 볼 수 있다. 상속은 굉장히 강한 결합(coupling)이다. 반드시 써야하는 곳에서만 쓰고 사용하지 않는 것이 좋다. 왜냐하면 좋은 객체는 결합도는 낮은게 좋기 때문이다. 잘못 상속 받았을 경우에 오는 타격이 너무 크기 때문에 그렇다. 리스크가 정말 크지만 어쩔 수 없이 사용하는 것이라고 생각하자.

```java
[접근제한자] [abstract|final] class className extends parentClass {
    ...
}
```

아무것도 상속받지 않으면 java.lang.Object를 상속한다. 모든 클래스는 기본적으로 object를 상속받는 것이다. 모든 클래스의 최상위 클래스는 object가 되는 것이다.

### 부모 타입으로 자손 타입을 참조

지금까지는 참조 타입이 인스턴스 타입과 같았는데 이러한 경우엔 다르다.

```java
Car car = new Bus();
```

참조하는 것이 Car인데 인스턴스는 Bus다.. `버스는 자동차(의 한 종류)다` 이런 말이 되는 것이다. 컴파일 오류가 발생하지 않으려면 버스는 자동차의 자손이어야 한다. 그냥 bus bus = new bus 해도 되는데 왜 굳이 이런 방식으로 하는 것일까?

버스 인스턴스가 있는데 자동차의 기능만 이용하고 싶은 경우에 이렇게 사용하는 것이다. 굳이 버스의 모든 메서드를 사용하지 않고, 자동차의 기본기능만을 가져오는 것이다. 이렇게 되면 메모리에 올라간 인스턴스는 bus이지만 참조변수를 이용해서 직접 사용할 수 있는 메소드는 car의 메소드들 밖에 사용하지 못하는 것이다. 필요에 의해서 해당 부분만 인스턴스가 취하는 것이라고 볼 수 있다.

### setter, getter

필드를 선언할 때는 보통 외부에서 접근하지 못하도록 `private` 접근제한자를 사용하곤 한다. 외부에서 필드에 직접 접근하지 못하는 정보 은닉을 한 것이다. 그렇기에 필드에 접근하는 방법을 method로 정해주는데, 이를 setter getter라고 한다. this는 내 자신 인스턴스를 말한다.

```{code-block} java
:caption: setter getter
:lineno-start: 1

public class Book{
  private int price; // field

  //setter
  public int getPrice(){
    return this.price; // instance variable
  }

  //getter
  public void setPrice(int price){ //  local variable
    this.price = price;
  }
}
```

이러한 것들을 `property`라고 한다. 여기서는 price property이다. field price는 클래스가 가지는 것이고, price property는 getter, setter를 말하는 것이다. 기본적으로는 사용하지 않지만 spring을 배우면 사용하게 된다.

## object 오버라이딩 메소드

### toString()

오버라이딩 전문 메소드들이다. 자식이 구현되는 것은 oop 쪽에서 확실하게 배웠다.

```java
public class CarExam3{
  public static void main(String[] args){
    Car c1 = new Car();
    System.out.println(c1); // prinln(Object x)
    // '자동차!!' 라고 출력된다.
  }
}
```

```java
public class Car{
  public void run(){
    System.out.prinln("전륜구동으로 달리다.");
  }

  @Override
  public String toString(){
    return "자동차!";
  }
}
```

부모타입의 변수로 자식 인스턴스를 참조할 수 있다. 조상타입의 변수로 후손 인스턴스를 참조할 수 있다. Car c1 = new Bus(); bus는 car의 자식이기 때문에 문제가 나지 않는다. 아무것도 상속받지 않으면 기본 object를 상속받는다. Object o1 = new Bus(); 이런 식으로 해도 전부 괜춘하다.

System.out.println(o1.toString()) == System.out.println(o1); 과 같은 것이다. 내부적으로 작동하는 것은 동일하다.

### equals()

답이 같은지를 묻는 것이다. 진리값을 return 해줄 것이다. 반드시 오버라이딩해서 사용해줘야한다.

### hashCode()

HashSet, HashMap이라는 자료구조 객체들이 존재한다. 여기서 equals 메소드를 잘 오버라이딩 해줘야한다.

## 생성자

- 인스턴스를 생성할 떄 사용한다.
- 어떤 값을 가지고 인스턴스가 만들어지게 하고 싶다면 생성자를 사용한다.
- 클래스 작성시 생성자를 하나도 만들지 않았다면 자동으로 기본 생성자가 생성된다.
- 기본 생성자는 매개변수를 하나도 받지 않는 생성자를 말한다.

생성자는 return 하는 타입이 없고, 메서드랑 비슷하다. 그리고 클래스 이름과 같아야한다.

```java
public class Car{
  public Car(){//default constructor
    System.out.println("자동차생성!");
  }

  private String name; // 필드는 가지는 것이다.
  public Car(String name){//with name constructor
    this.name = name; //this.name = field, name = local variable
  }
  public void printName(){
    System.out.println("car name : " + name);
  }

  @Override
  public String toString(){
    return "car!!";
  }
}
```

생성자를 하나라도 만들면 기본 생성자가 안 만들어지게 된다. 생성자를 만들면 그 방식을 반드시 사용해야하는 것이다. 필드를 외부에서 사용하려면 getter setter를 만들어줘야한다.

```java
public class User(){
  private String email;
  private String password;
  private String name;


  public User(String name, String email){
    this(name, email,password:null);
    //자신의 생성자를 호출하는 방식으로 하면 중복을 줄일 수 있다.
    // 많이 받아주는 것을 this로 호출하는 것을 하면 코드를 줄일 수 있다.
    // super 생성자를 제외하고는 첫번째 줄에 나와줘야한다.
  }

// 생성자 오버로딩
  public User(String name, String email, String password){
    this.email = email;
    this.name = name;
    this.password = password;
  }

  public String getEmail(){return email;}
  public String getName(){return name;}

  @Override
  public String toString(){
    return "User{" +
          "email='" + email + '\'"+
          ", name='" + name + '\'' +
          '}';"
  }
}
```

생성자에서 넣어준 것을 return만 해주는 것을 불변객체라고 말한다. getter는 있는데 setter는 없기 때문에 값으르 바꿔주는 것이 안되는 것이다. 이런 불변객체는 어떤 값을 가지게 한다음에 외부에 전달할 때 이런 객체를 사용한다.

### this

- this는 인스턴스 자기 자신을 참조할 때 사용하는 키워드
- this() 생성자는 자기 자신의 생성자를 말한다.
- this() 생성자는 생성자 안에서만 사용가능하다.
- this() 생성자는 생성자 안에서 super() 생성자를 호출하는 코드 다음이나, 첫번째 줄에 위치해야한다.

### super()

::::{grid} 3
:gutter: 3
:class-container: full-width

:::{grid-item-card} Car2.java

```java
public class Car2 {
  public Car2(String name){
    super(); // 자동으로 생성되는 부분
    System.out.println("Car2() 생성자 호출");
  }
}
```

^^^

:::

:::{grid-item-card} Car2Exam.java

```java
public class Car2Exam {
  public static void main(String[] args){
    Car2 c1 = new Car2(name:"surdarla");
    Bus2 b1 = new Bus2();
  }
}
```

^^^
content
:::

:::{grid-item-card} Bus2

```java
public class Bus2 extends Car2{
  public Bus2(){
    super(name:"Bus!!"); // 자동으로 생성되는 부분
    System.out.println("Bus2기본생성자")
  }
}
```

^^^
**부모가 기본 생성자가 없으면** 자식의 생성자에서는 부모의 생성자를 직접 super로 호출을 해줘야한다.
:::
::::

- super는 인스턴스 부모를 참조할 때 사용하는 키워드이다.
- super() 생성자는 부모 생성자를 의미한다.
- super() 생성자는 생성자 안에서만 사용가능하다.
- super() 생성자는 생성자 안에서 첫번째 줄에만 올 수 있다.
- 생성자는 무조건 super() 생성자를 호출해야한다. 사용자가 super() 생성자를 호출하는 코드를 작성하지 않았다면 자동으로 부모의 기본 생성자가 호출된다.
- 부모클래스가 기본 생성자를 가지고 있지 않다면, 사용자는 반드시 직접 super() 생성자를 호출하는 코드를 작성해야한다.

## 추상클래스

추상클래스는 인스턴스가 될 수 없다. 추상 클래스를 상속받는 자손이 인스턴스가 된다. `abstract` 키워드를 사용하여 클래스를 정의한다. 추상클래스는 보통 1개 이상의 추상 메서드를 가진다.(추상메서드가 없어도 오류가 발생하진 않는다.) public abstract class className {....} 이런식으로 생겼다.

파이썬에서 abc(abstract base class)가 생각나는 부분이다. dict나 여러가지 자료구조나 자료형(타입)에 대해서 기본적인 틀을 잡아놓은 것이라고 보면 된다. 반드시 필수적으로 들어가야할 기능들에 대해서 높은 수준의 추상화를 진행해서 잡아놓은 틀이라고 생각하면 될 것이다.

부모가 가지는 추상클래스는 부모에선 구현을 틀만 해놓고 자식이 오버라이드해서 수정해야한다.

### template method pattern

추상클래스는 template method pattern에서 많이 사용된다. 여기서 final protected abstract에 대해서 이해하고 넘어가야한다.

```java
public abstract class Controller{
  // final이 붙으면 override 할 수 없다.
  protected final void init(){
    System.out.println("초기화하는코드");
  }
  protected final void close(){
    System.out.println("마무리하는코드");
  }
  // 이건 자식이 무조건 override 해야하는 부분.
  protected abstract void run();

  public void execute(){
    this.init();
    this.run();
    this.close();
  }
}
```

```java
package com.example.myproject;
import com.example.fw.Controller;

public class FirstController extends Controller{
  @Override
  protected void run(){
    System.out.prinln("별도 동작 코드 1111");
  }
}
```

```java
package com.example.main;
import com.example.fw.Controller;
import com.example.myproject.FirstController;

public class ControllerMain {
  public static void main(String[] args){
    Controller c1 = new FirstController();
    c1.execute();
  }
}
```

### final

- 부모가 될 수 없는 클래스
- 상속을 금지시키려면 클래스를 정의할 때 final 키워드를 사용한다.
- `public final class className {}` 이런 식으로 정의한다.
- String class에 대한 api를 보면 final로 되어있다.
  - `pulic class MyString extends String{}` 이런식으로 하려면 에러난다.
  - 기본적으로 String class는 불변 객체이다.(immutable)

new를 사용하면 heap 메모리에 각자 다른 객체들이 만들어진다. "hello" 이런식으로 만들어서 변수에 지정하면 같은 하나의 것로 인식하지만 new를 사용하면 항상 다른 객체이다.

```java
package com.example

public class StringExam2{
  public static void main(String[] args){
    String str1 = "hello";
    String str2 = new String(original:"hello");

    if (str1 == str2){
      System.out.prinln("str1과 str2는 동일한 객체다.")
      // 다른 객체라고 나온다.
    }
    if (str1.equals(str2)){
      System.out.println("str1과 str2의 값이 같다.");
      // 같다고 나온다.
    }
    String s = str1.toUpperCase();
    System.out.println(s); // HELLO
    System.out.println(str1); // hello
  }
}
```

String의 모든 메서드는 새로운 객체를 반환한다. String은 위에서 말했듯이 final 불변 객체이고 기존의 것이 변하는 것이 아니다. 메서드가 적용된 문자열은 새로운 객체로 메모리에 올라가고 이에 대해서 새로운 변수로 받아줘야지 사용가능하다는 것을 기억하자.

String이랑 비슷하지만 내부가 변하는 것은 `StringBuffer` class이다. `StringBuilder`도 존재한다. String은 잘못사용하면 성능저하가 극단적으로 발생한다. 저번에 풀어봤던 문제도 String으로는 시간초과가 났지만 StringBuilder로 계속 String 하나에 대해서 변화를 주는 방식으로 하니깐 문제가 통과가 됬었다.

## 접근제한자

| 접근제한자 | 클래스내부 | 동일패키지 | 하위클래스 | 그외  |
| :--------: | :--------: | :--------: | :--------: | :---: |
|   public   |     ✔️      |     ✔️      |     ✔️      |   ✔️   |
| protected  |     ✔️      |     ✔️      |     ✔️      |   ✖️   |
|  default   |     ✔️      |     ✔️      |     ✖️      |   ✖️   |
|  private   |     ✔️      |     ✖️      |     ✖️      |   ✖️   |

- default는 아무것도 안쓰는 경우가 디폴트이다.
- method는 이름만봐도 내용이 직관적으로 알 수 있어야한다.
- 구린향기가 나는게 아니라 좋은 향기가 나는 코드가 되려면 깔끔하게 코딩을 할 수 있어야한다.

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
