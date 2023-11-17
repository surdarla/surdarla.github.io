(perceptron)=
# Perceptron

1957년 프랑크 로젠블라트가 고안한 알고리즘이다. 신경망의 기원이 되는 알고리즘이다. 퍼셉트론은 다수의 신호를 입력으로 받아 하나의 신호를 출력한다. 신호는 전류나 강물처럼 흐름이 있는 것으로 생각하면 편하다. 1은 true로 흐르고, 0은 false로 안흐른다를 표현하다.

신호의 출발점이 두 개라고 생각해보자. 해당 출발점 두 개를 `neuron, node`라고 부른다. 신호가 출발하면 각각 고유한 가중치 $w$를 곱해주게 된다. 이 가중치를 곱한 것들의 합이 정해진 한계를 넘어가면 1을 출력한다. 이러한 경우에 `뉴런이 활성화된다`라고 한다. 그 값을 임계값`threshold`라고 하며 $\theta$로 나타낸다. 수식으로 나타내면 아래와 같다.

$$
y = \begin{cases}
    0(w_1x_1 + w_2x_2 <= 0)\\
    1(w_1x_1 + w_2x_2 > 0)
    \end{cases}
$$

- 퍼셉트론은 입출력을 갖춘 알고리즘이다. 입력을 주면 정해진 규칙에 따른 값을 출력
- 가중치, 편향을 매개변수로 설정한다.
- AND,OR 게이트 논리회로를 표현할 수 있으나, 단층 퍼셉트론으론 XOR는 표현이 불가능하다.
- 2층으로 쌓으면 표현이 가능하다. 이는 비선형적인 표현이 가능해 지기 때문이다.
- 다층 퍼셉트론은 컴퓨터를 표현할 수 있다

## Reference

- 밑바닥부터 시작하는 딥러닝 : 사이토 고키

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
