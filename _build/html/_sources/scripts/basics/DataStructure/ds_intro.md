# 자료구조

CS에서 데이터를 구조적으로 표현 및 구현하는데 필요한 알고리즘에 대해 공부하는 기초이론을 말한다. 즉 데이터를 어떻게 표현하는지에 대해서 공부하고 이에 대해서 구현할 수 있으면 된다는 것이다. 알파벳처럼 너무나도 기본이 되는 부분이기 때문에 해당 부분에 대해서 제대로 파악하고 있지 못하면 나중에 힘들게 된다. 리스트, 스택, 큐, 환형큐, 힙, 트리, 그래프 7가지 기본개념을 숙지하기 와 같은 의미라고 보면 된다.

컴퓨터의 메모리는 1차원 구조라고 볼 수있다. (0,1,0,1,...) 현실의 다차원 데이터를 다루기 위해서는 이것을 1차원인 선형으로 바꾸는 것이 필요하다. 기초 알고리즘에서는 이것을 배운다. 2차원 배열, 이진트리, 그래프 등의 자료구조가 2차원을 1차월으로 projection하는 것이라고 볼 수 있다.

더 나아가서 3차원 데이터를 다루고, 3차원 데이터 이상의 다차원 데이터를 처리하는 자료구조를 만나게 될 것이다.

## 추상적 자료형과 자료구조

추상적 자료형이란 알고리즘이 문제를 해결하는데 필요한 자료의 형태와 자료를 사용한 연산들을 수학적으로 정의한 모델이다. 그러니깐 추상적 자료형을 구현하면 자료구조가 되는 것이다. 마치 파이썬의 객체지향 프로그래밍에서 특정 class가 가져야할 일정한 틀을 부여하는 abstract base class(ABC)와 같다고 볼 수 있다.

예를 들면, 후입선출의 성질을 가지는 추상적 자료형이 필요하니 pop push를 가지도록 `stack 스택`이라는 추상적 자료형을 정의한다. 그리고나서 그것을 구현해서 함수 호출을 관리하는데 사용하는 구현제(자료구조)를 `콜 스택`이라고 부르는 것이다.

- 조금이라고 구현방법이 정해져 있으면 자료구조이다.
- 반면 구현방법이 전혀 정의되어 있지 않으니 추상적 자료형이다. 큐도 매한가지

```{tableofcontents}
```

## Reference

- [자료구조 wiki](https://namu.wiki/w/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)
- [Python docs queue](https://docs.python.org/ko/3.13/library/queue.html)