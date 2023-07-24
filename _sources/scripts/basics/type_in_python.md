# Type in python

C를 잘 아는 것은 아니지만 C를 시작하면 맨 처음에 변수를 정의할 때 변수의 타입을 함께 정의하곤 했다. 이러한 언어를 정적인 언어라고 한다. 파이썬은 C와 다르게 동적 언어로 알려져 있으며 이러한 언어의 특징은 C와는 반대로 특정 변수의 타입이 중간에 바뀌어도 되고, 처음에 명시하지 않아도 변수를 사용할 수 있다는 것이다. 하지만 변수의 Type을 지정하고 사용하는 것은 에러 관리와 코드 유지에 중요한 역할을 한다.

## 타입 Type?

```{figure} ../../images/data_type_1.png
---
height: 400px
name: data_type_fig1
---
메모리 상에서 변수와 값의 선언
```

```{margin} byte

1byrte(8bit)로 표현할 수 있는 경우의 수, 값의 총 개수는 $2^8 = 256$개로 아스키코드(ASCII)를 표현할 수 있다. 4byte(32bit)에서는 4,294,967,296(2^32)개 이며 범위는 -2,147,483,648 ~ 2,147,483,648의 정수 범위이다.
```

프로그래밍을 한번에 정리한 좋은 문장이 있길래 가져와 보았다.

```{epigraph}
프로그래밍은 **변수를 통해 값을 저장하고 참조**하며 연산자로 값을 연산, 평가하고 조건문과 반복문에 의한 흐름제어로 데이터의 흐름을 제어하고 함수로 재사용이 가능한 구문의 집합을 만들며 객체, 배열 등으로 자료를 구조화하는 것이다.

-- modern javascript deep dive
```

변수(variable)은 `값(value) = 데이터(data)`의 메모리 상의 위치,주소(memory address)를 기억하는 저장소이다. 그러니깐 우리는 값을 저장하고 다시 불러올 때 컴퓨터처럼 모든 메모리 주소를 기억할 수 없으니, 인간이 이해하기 쉬운 `identifier 식별자 = variable 변수`로 들락날락 하는 것이다. 객체 지향 프로그래밍 할 때 처음 나오는 것이 서로 다른 객체라는 것은 메모리에서 서로 다른 공간(다른 주소)에 저장되었다는 것을 의미한다고 하며 '=='로 속성값은 같을지라고 'is'로 id값 주소값을 비교하면 다를 수 있다고 말한다. 즉 값은 같아도 주소는 다르면 그것은 변수가 다른 것이고, 객체로는 다른 객체로 볼 수 있다. 파이썬에서 주소값을 확인하려면 `id(object)` 함수를 사용하면 된다.

> id(object)
>> Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
>> CPython implementation detail: This is the address of the object in memory.

데이터 타입은 무엇인가? 코드 상의 데이터는 메모리에 저장하고 참조될 수 있어야 한다. 메모리에는 2진수 데이터를 효율적으로 저장하기 위한 규칙이 존재하고, 그 기본적인 약속된 형태가 `data type`이다. 기본적인 sty, int, boolean, none 과 같은 타입에 대한 설명은 pass.

```{figure} ../../images/data_type_2.jpg
---
height: 400px
name: data_type_fig2
---
기본적인 data type in python
```

파이썬은 3.5v 이상부터 Typing을 지원하고 있다. vscode를 사용한다면 기본적으로 pylance를 사용할 것이고, pyrigth의 기능을 pylance가 이미 하고 있기 때문에 굳이 뭔가를 깔 필요는 없을 것이다. 기본적인 사용 방법은 `variable: type = default_value` 이런 식으로 사용한다. arg_parser를 사용할 때나, class 내부의 변수를 구조화 할 때 사용한다. def의 return값을 지정할 때는 `-> type`을 하면 된다.

```python
a: int = 3
def temp_func(temp: str) -> str:
    return temp.strip()
```

## Tpye 종류

1. **Union** -
`Union[str,bytes,None]` 처럼 하나의 함수의 인자에 여러 타입이 사용될 수 있을 떄 사용한다. 3.10v 이상 부터는 `str | bytes | None` 이렇게도 사용가능하다.
2. **Optional** -
Union은 Optional로 대체가능하다. `Optional[str]`로 하면 str or None을 받는다는 의미다.
3. **List, Tuple, Dict** -
3.9v 이상부터는 typing에서 List,Tuple,Dict를 import하지 않아도 가능하다.
4. **Callable** -
`Callable[[arg1type,arg2type],returntype]` 함수를 인자로 가지는 경우. 만약 return 인자만 지정하고 싶다면 `Callable[...,returntype]`로 하면 된다.
5. **Type** -
class 객체는 해당 타입을 그냥 명시하면 된다. 혹은 `Type[class_name]` 직접 class 이름을 넣을 수도 있다.
6. **TypedDict** -
딕셔너리의 경우에는 밸류의 타입이 하나로 고정되지는 않을 수 있다. 상속받는 클래스를 만든 다음 key-value type matching을 시켜주면 된다. 혹은 `dataclass`로 대체해서 사용가능하다.
7. **Generator, Iterable, Iterator** -
`Generator[YieldType, SendType, ReturnType]` - sendtype을 input으로 받고 - yieldtype을 output하며 - returntype을 예외경우에 뱉는다.
8. **Any** -
쓰지마라,
9. **ParamSpec** - 가변 위치 인자(*args)와 가변 키워드 인자(**kwargs)를 받고, 이들의 타입을 ParamSpec으로 지정합니다. 또한, 반환 타입으로 Tuple[ParamSpec, ParamSpec]을 사용하여 args와 kwargs의 타입을 나타낸다. 3.10v이상부터 가능하다/

```python
from typing import ParamSpec, Tuple

def my_function(*args: ParamSpec, **kwargs: ParamSpec) -> Tuple[ParamSpec, ParamSpec]:
    return args, kwargs
```

## Reference

- [솔라쿠아 - 파이썬 Typing 파헤치기 - 기초편, 심화편](https://sjquant.tistory.com/68)
- [모던자바스크립트 deep dive - data type & variable](https://poiemaweb.com/js-data-type-variable)
- [TechNote.kr - Python - id(), object의 unique 값(memory address)를 보여주는 함수](https://technote.kr/289)
-
