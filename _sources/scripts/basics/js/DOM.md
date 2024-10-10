(DOM)=
# DOM

> HTML/XML 문서는 브라우저 안에서 DOM 트리로 표현된다
> 문서객체모델(DOM)에 따르면 모든 HTML tag는 객체이다.

문자들도 역시 객체다. 이런 모든 객체는 자바스크립트를 통해서 접근할 수 있고, 페이지를 조작할 때 이 객체를 사용한다.

`html`은 루트 노드가 되고 `head`,`body`는 자식노드가 되고 그 밑으로 또 자식들이 들러붙는다. 태그는 요소 노드가 되고 트리구조를 형성한다. 문자는 텍스트 노드가 된다. 이 외에 HTML 내의 모든 것은 DOM을 구성한다. 심지어 주석까지 된다.

Javascript는 이러한 DOM의 요소들에 대해서 접근할 수 있는 언어이고, 그 시작은 `document`객체에서 시작한다. document 객체는 그 자체가 html 페이지 하나를 의미한다.

    <html> = document.documentElement
    <body> = document.body
    <head> = document.head

    document.body.childNodes는 iterable 유사배열객체인 collection이다.
    해서 이걸로 for문을 돌면서 객체의 속성을 변경하는 작업도 가능하다.

    만약 배열의 메서드를 사용하고 싶으면
    Array.from(document.body.childNodes).filter 와 같은 식으로 사용할 수 있다.

## DOM 요소 찾기

### getElementByID, getElementsBy*

> - 뒤에 나오는 프로퍼티를 이용해서 해당 노드를 찾아주는 메서드
> - `getElementsBy`로 찾아온 것들은 live 컬랙션이다. 문서에 변경이 있을 때마다 자동 갱신되어 최신 상태를 유지한다.

### querySelector 표기법

1. `.class`
   - html요소의 class 이름을 기반으로 요소를 선택하는 선택자
   - 해당 클래스를 가진 모든 요소를 선택한다 - 마치 `querySelectorAll(class)`처럼
   - 여러 클래스를 동시에 지정하려면 공백으로 구분
   - 저런 방식으로 css 파일 내부에서도 정의된다.
2. `#id`
   - id는 document내에서 고유해야한다
   - 보통 하나의 요소에 대해 고유한 식별자로 사용된다.
3. `:nth-child(n) elem`
   - 앞에서 선택한 요소들 중 n번째를 선택

**DOM기반 node 검색 methods**

|          method          |    search     | 요소 호출 | collection갱신 |
| :----------------------: | :-----------: | :------: | :------------: |
|     `querySelector`      | `CSS 선택자`  |    ✔     |       -        |
|    `querySelectorAll`    | `CSS 선택자`  |    ✔     |       -        |
|     `getElementById`     |     `id`      |    -     |       -        |
|   `getElementsByName`    |    `name`     |    -     |       ✔        |
|  `getElementsByTagName`  | `tag` or `'*'` |    ✔     |       ✔        |
| `getElementsByClassName` |    `class`    |    ✔     |       ✔        |

**알아두면 좋을 methods**

|method|do|
|:-:|:-:|
|`elem.matches(css)`|일치하는지 여부 검사|
|`elem.closest(css)`|가장 가까운 조상요소 탐색|
|`elemA.contains(elemB)`|elemB가 elemA에 속하거나, elemA==elemB일때 참 반환|

## DOM 요소 변경하기

### toggle

DOM은 하나의 class만 가지고 있지 않을 확률이 굉장히 높다. 해당 클래스가 없으면 그 클래스를 추가하고 있으면 없엔다(마치 스위치처럼).

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
    // const clickedClass = "clicked";
    // if (h1.classList.contains(clickedClass)){
    //     h1.classList.remove(clickedClass);
    // } else {
    //     h1.classList.add(clickedClass);
    // }
    h1.classList.toggle("clicked")
}
h1.addEventListener("click",handleTitleClick);
```

## referance

- [DOM 트리](https://ko.javascript.info/dom-nodes)


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
