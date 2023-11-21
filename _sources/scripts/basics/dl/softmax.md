(softmax)=
# softmax

> k개의 실수로 이루어진 벡터를 k개의 가능한 결과에 대한 확률 분포로 변환하는 함수

로지스틱 함수([Logistic function](sigmoid))의 다차원 확장이며, 다항 로지스틱 회귀나 인공신경망에서 사용된다.

소프트맥스 함수는 주로 다중 클래스 분류 문제에 사용되는 활성화 함수 중 하나다. 소프트맥스는 input을 확률로 변환하며, 각 클래스에 대한 확률 분포를 생성한다. 주로 다음과 같은 상황에서 사용된다. 이진 분류와 비교해서 생각해보면 좀 더 용이하다. [sigmoid](sigmoid)는 yes or no 만을 위해 사용되었다면, 여러 등급이나 클래스로 나누는 경우에 softmax를 사용하는 것이라고 보면 된다.

```{figure} https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQGFKh%2FbtqPQtew8NG%2FP5e54TRwt9fZqmXi55866k%2Fimg.jpg

softmax activation function 개요
```

1. **다중 클래스 분류** : 주어진 입력에 대해 여러 클래스 중 하나를 선택하는 문제(이미지 분류, 자연어 처리 언어 모델)
2. **확률 분포 생성** : 각 클래스에 속할 확률을 계산하고, 가장 확률이 높은 클래스를 선택하는데 사용됨

softmax function을 통과한 모든 output값들의 합은 1이 된다. 이를 다시 말하면 `확률(Probability)`가 되는 것이다. sigmoid가 output layer값을 보고 threshold(보통 0.5)보다 크면 1, 작으면 0으로 이진분류 밖에 못하는데, softmax output layer는 나오는 모든 값들을 normalizing 해버리고, 각각에 대한 확률을 구해낸다.

$$
\text{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{j=1}^Ke^{z_j}}
$$
input vector z에 대해서 output은 i번째 클래스에 대한 확률을 말한다. $e^{z_i}$는 i번째 입력 요소의 지수 함수를 나타낸다.

```{figure} https://velog.velcdn.com/images%2Fguide333%2Fpost%2F05653beb-0e79-48d8-90d9-3744253421d5%2FScreenshot%20from%202021-05-17%2011-10-04.png

softmax function
```

## softmax 구현

```python
import numpy as np
def softmax(x):
    e_x = np.exp(x-np.max(x)) #오버플러우 방지를 위해 입력값 중 최대값을 빼줌
    return e_x / e_x.sum()
x = np.array([1,1,2])
y = softmax(x)
print(y) # [0.2,0.2,0.6]
```

## reference

- [노마드공학자 - softmax regression](https://limitsinx.tistory.com/36)

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
