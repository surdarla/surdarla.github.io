# JS Challenge

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Nov 29 Wed 13:15, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

> web page interactive browser language

JS는 모든 브라우저에 내장되어 있어서 설치가 필요없는 언어이다. front-end에 사용할 수 있는 유일한 언어라는 장점이 있다. 니코쌤은 JS를 프랑켄슈타인 언어라고 말한다. 그만큼 어쩔 수 없이 필요에 의해 사용하곤 있지만 완벽한 언어라고는 할 수 없기에 지속적인 패치와 수정으로 고쳐나아가는 중이라는 것이다.

JS는 주로 클라이언트 측 스크립트로 사용된다. 이에 반해서 서버 측에서는 Node.js가 JS가 실행되는 환경을 제공한다. Node.js는 오픈소스 서버측 런타임으로, JS를 사용하여 웹 App을 개발하고나서, 이를 실행할 수 있게 하는 `platform`이다. JS가 브라우저 상에서 동작하는 코드만을 말한다면, node js는 API서버, web server, web app, 실시간 애플리케이션 등 다양한 유형의 서버측 어플리케이션을 개발할 수 있다. 원래는 클라이언트 측만에서 사용되었는데 이것이 백 단으로까지 하나의 언어로 구축할 수 있다는데 에서 node.js의 의미는 js에 크다고 볼 수 있다.

## variables : const, let

> const를 사용하되 변해야 할 경우가 있는 것만 let 사용

`const`는 말그대로 `상수`로 변할 수 없는 값을 변수로 지정할 때 사용하는 syntax이다. 이에 대한 반대로 `let`을 사용하는데 이에 들어간 변수는 변할 수 있는 것을 의미한다. 이러한 것들은 js가 변화하면서 생긴 syntax로 변수에 대한 명시를 하기 위해서 생겨난 것이다.

`var`는 아주 오래된 것으로 언제 어디서든 변화할 수 있는 말그대로 변할 수 있는 변수이다. 그런데 이것은 사용하지 않는 것이 좋은게 '언어로부터 전혀 보호를 받지 못한다'.

## boolean : undefined, null

true, false는 기본적인 값이므로 넘어간다

> undefined : 변수 선언 + 값 할당 x
> null : 변수에 null값이 할당됨. 즉 정의는 됨.

변수에 값을 배정한지 안한지에 따라서 다른 것으로 보면 된다. undefined는 아예 값을 배정해 주지 않은 것이다. null값이 지정된 것은 null data type을 가진다.

## array : []

javascript에서 배열을 initialize 초기화 하는 방법에는 여러가지 방법이 존재한다. 각 방법은 특정 상황에 적합하며, 다양한 방식으로 생성 및 초기화가 가능하다. 상황에 따라서 다른 방법에 대해서 알아보자.

1. 리터럴
   1. 가장 간단하고 직관적인 방법
   2. `let arr = [1,2,3];`
2. Array 생성자
   1. 지정된 크기의 새 배열을 생성한다. 이 방법은 배열의 길이만 지정한다. 나중에 요소를 추가한다.
   2. `let arr = new Array(10);` 길이 10의 배열 생성
3. `Array.of` 메서드
   1. 주어진 인자들로 배열을 생성한다.
   2. `let arr = Array.of(1,2,3);`
4. `Array.fill` 메서드
   1. 배열을 특정 값으로 초기화 한다. 고정된 값으로 배열을 채움. 0으로 만들어진 arr 만들때 유용
   2. `let arr = new Array(5).fill(0);`
5. `Array.from` 메서드
   1. 배열과 유사한 객체나 반복 가능한 객체로부터 새 배열 만들기
   2. `let arr = Array.from({length:5},(_,index) => index);`
   3. 0~4까지의 값을 가진 배열을 생성
6. `spread` 연산자
   1. 기존 배열이나 반복 가능한 객체를 새 배열로 복사
   2. `let arr = [..."123"];`
   3. 문자열"123"을 배열해서 \['1','2','3'\]으로 변환
7. `map`,`forEach`
   1. 기존 배열을 기반으로 새로운 배열을 생성하거나 기존 배열 수정
   2. `let arr = [1,2,3].map(x => x*x)`

```{admonition} forEach 주의점
:class : topic, margin

forEach 메서드를 사용하여 배열을 초기화하면, 기존의 각 요소에 대해 주어진 함수를 실행한다. 주의점은 **새로운 배열을 반환return 하지는 않는다는 것**이다. forEach는 주로 기존 배열을 변경하거나, 새로운 효과(사이트 이펙트)를 생성하는데 사용된다.

기본적인 javascript가 html을 실시간으로 동적으로 변화하게 하는 브라우저 언어로 만들어졌기 때문인 것을 이런 특징들로 다시금 알 수 있다.
```

```javascript
let originArr = [1,2,3];
let newArr = [];

originArr.forEach((x) => {
  newArr.push(x*x);
});

console.log(newArr);
// [1, 4, 9];
```

## function

함수화를 한다는 것은 `코드를 캡슐화`한다는 것이다. 반복되는 부분을 캡슐화해서 `call`해와서 사용함으로써 코드를 간결화하고 가독성을 높이는 것이다. python에서는 `def`를 사용해서 너무나도 익숙하지만 js에서는 조금 다른 것으로 보인다.

```javascript
function 함수이름(매개변수){
    변수를 활용한 함수 작동내용;
}
```

보통 이런식으로 만들어진다. 이 부분을 '함수 선언'이라고 부른다. 함수는 코드의 한 부분을 잘라내서 동작하는 것이기 때문에 동작하는 것을 이름으로 명확하게 규정해야하며, 하나의 동작만을 정확하게 하는 것이 좋다. 주석을 달게 된다면 해당 주석은 명확해야하고 함수의 동작은 주석의 순서대로 진행하는 것이 좋다. 간결한게 최고다.

변수에 대해서 정리가 필요할 것으로 보인다.

### Variable, Parameter, Argument

- argument : 함수 호출시 parameter에 전달되는 `실제 값`
- parameter : 함수 선언시 같이 정의하는 `변수`

1. 지역 변수(local variable) : 함수 밖에서는 의미 없음
2. 외부 변수(outer,global variable) : 지역변수 없는 경우만 사용가능

함수에 전달된 매개변수(parameter)는 복사된 후 지역 변수가 된다. 당연한 거지만 내부적으로 이렇게 동작된다는 것을 한 번 정도는 생각해보는 것이 좋을 것으로 보인다.

### return

- return이 없거나, return만 있으면 `undefined`를 반환한다.

### 함수 선언문 vs 함수 표현식

함수 선언문은 실제로 정의하는 흐름을 지나기 전에도 호출할 수 있다. 전역 함수 선언문은 스크립트 어디에 있느냐에 상관없이 어디서든 사용할 수 있다. JS는 스크립트를 실행하기 전에, 준비단계에서 전역 함수 선언문을 전부 찾아서 생성하고.. 그 이후에 실행된다.

함수 표현식은 실제 실행 흐름이 해당 함수에 도달했을 때 함수를 생성한다. 때문에 표현식으로 정의된 함수는 스크립트 흐름이 표현식을 지나기 전까지는 사용이 불가능하다.

그럼 언제 사용해야하는가?

```javascript
let age = prompt("나이를 알려주세요.", 18);

let welcome;

if (age < 18) {

  welcome = function() {
    alert("안녕!");
  };

} else {

  welcome = function() {
    alert("안녕하세요!");
  };

}

welcome(); // 제대로 동작합니다.

// ?를 사용해서 단순화한 버전
let age = prompt("나이를 알려주세요.", 18);

let welcome = (age < 18) ?
  function() { alert("안녕!"); } :
  function() { alert("안녕하세요!"); };

welcome(); // 제대로 동작합니다.
```

위의 코드를 보면 우선 함수를 변수로 선언만 해놓고 if, else문 안에서 = 뒤에 만들어 주고 있다. 그러니깐 경우에 따라서 함수를 달리 선언해 주어야 할 경우에 특히 유용하다. `함수를 미리 만들어놓지 않는 특성` 때문에 사용해야할 경우가 있고, 그냥 전역 함수로 선언해 버려야할 경우도 있는 것이므로, 두 경우를 둘 다 알고 있는 것이 유용할 것으로 보인다.

### 콜백 함수

> 함수를 함수의 인자(argument)로 전달하고, 필요할 경우 "나중에 호출(called back)"하는 함수

## document

JS가 중요한 지점이 나온다. 우리가 마주하는 html은 말그대로 대문과 같은 보이는 지점이다. js에서는 `document`가 html을 말하는 것이다. document에는 아주 많은 properties가 존재하고 이것에서 정보를 가져오고 수정함으로써 다양한 작업을 할 수 있게 해준다.

html은 정적인 리소스이다. 사용자에게 표시할 화면은 처음 html로 만들고 나면은 그걸로 변경하는 것은 불가능하다. html로 변경은 불가능하지만 js로는 가능하기에 사용하는 것이다. 더 나아가 server와 통신하여 복잡한 처리를 하거나, server-client 사이에서 주고받는 과정은 html을 통해서 이루어 지는 것이 아니라  js를 통해서 이루어진다.

## class 바꾸기

something for nothing

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
