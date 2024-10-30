# 일회성

## anonymous class

이름 없는 클래스를 만드는 방법에 대해서 알아보자.

```java
Car car = new Car(){
    public void run() {
        System.out.println("Car를 상속받는 이름없는 객체가 run메소드 override");
    }
}
```

```java
// CarExam.java
public class CarExam {
    public static void main(String[] args) {
        Car car = new Car() {
            @Override
            public void a() {
                System.out.println("이름없는 객체의 a()메서드 오버라이딩");
            } // override
        }; //car
        c1.a()
    } //main
}
```

- new 생성자() {...}
- 생성자 뒤에 중괄호가 나오고 코드를 오버라이딩 하여 보통 구현함.
- 주로 일회성으로 사용되는 클래스를 구현할 때 활용된다.
- 간결하게 클래스 정의하고 인스턴스화할 수 있다.
- 마지막에 ; 를 붙여줘야한다. 객체 생성하는 문장이기 때문

```java
public class MyRunnableMain2{
    public static void main(String[] args){
        RunnableExecute runnableExecute = new RunnableExecute();
        runnableExecute.execute(new MyRunnable(){
            @Override
            public void run() {
                System.out.println("hello");
            }
        });
    }
}
```

이름 없는 객체를 생성하자마자 메소드에 넣어버려 준 것이다. 이런 것들은 재사용할 일이 없고 일회적으로만 사용할 때 사용하는 것이다.

## lambda

더 나아가서 이렇게 까지 할 수 있다.

```java
public class MyRunnableMain2 {
    public static void main(String[] args){
        RunnableExecute runnableExecute = new RunnableExecute();
        runnableExecute.execute(() -> {
            System.out.println("hello");
        });
    }
}
```

이렇게 하는 부분이 lambda interface이다. 이름 없는 객체를 간략화 시켜서 하는 것이다. 이런 경우는 메소드를 딱 하나만 가지고 있어야한다. spring api와 나중에 같이 사용하게 되면 편리한 것들을 할 수 있게 한다.
