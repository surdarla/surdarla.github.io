(json=)
# JSON

> Javascript Object Notation

javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷을 말한다. 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용된다. 서버에서 클라이언트로 데이터를 전송하여 표현하려거나, 반대로 클라이언트에서 서버로 데이터를 전송하는 경우를 말한다.

시작은 javascript에서 시작되었지만, 다른 언어들에서도 json을 다루는 기능을 기본적으로 내포하고 있다. python에서도 `import json`, `yaml`라든가하는 방법으로 읽고 변경할 수 있다. 기본적으로 python의 `dict`과 생김새가 비슷하고 구조적인 측면에서는 사실상 동일(key-value)하기 때문에 딕셔너리 객체를 만들고 json으로 바꾸는 방식으로 많이 활용된다.

`json`은 문자열 형태로 존재한다. 문자열이기 때문에 데이터 전송할 때 다른 data type으로 바꾸는 것에 대해서 신경쓸 필요가 없다. 데이터에 접근하기 위해서는 native json object로 변환될 필요가 있다. 로드한 다음 변수에 파싱하면 딕셔너리와 같은 문법으로 객체 내에 데이터에 접근할 수 있게 된다.

**Json 특이점**

- 순수 데이터 포맷이기에 메서드는 담을 수 없고, 프로퍼티만 담을 수 있다.
- "" 큰 따옴표만 사용한다.
- 따옴표로 묶인 문자열만이 프로퍼티로 사용될 수 있다.

## parsing, stringify

```{figure} https://scaler.com/topics/images/what-is-json-parse.webp
```

`parsing` string에서 native object로 변환하는 것을 말한다. 이와 반대로 네트워크를 통해 전달될 수 있게 객체를 문자열로 변환하는 과정은 `stringify`라고 한다. 이는 순전히 네트워크에 전달될 수 있는 데이터 타입은 문자열 밖에 없기 때문인 것으로 보인다. 문자열로 받아와서 내 작업환경 내의 변수들을 받아올 수 있도록 문자열을 객체로 변환하는 과정과 이의 반대를 말하는 것이다.

## referance

- [MDN - JSON으로 작업하기](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON)
