(attention)=
# Attention

#transformer, #attention

```{note} Attention
**a vector of importance weights**

in order to predict or infer one element, such as pixel in an image or a word in a sentence.
```

how strongly it is correlated with(or attends to) other elements and take the sum of their values weighted by the attention vector as the approximation of the target

이미지와 텍스트 상에서 하나의 원소는 pixel, word일 것이다. 이에 대해서 attention은 다른 것들과 연관성이 얼마나 강한 지를 표현하는 역할을 해준다. 그런데 이에 대해서는 그동안 seq2seq가 동일한 역할을 했었지만 long-term problem 때문에 멀리 있는 요소에 대한 기억력 감소로 attention 사용하게 된다. seq2seq는 2014년에 attention은 2015년에 transformer는 2016년에 각각 나왔다.

> the secret sauce invented by attention is to create **shortcuts between the context vector and the entire source input**. The weights of these shortcut connections are customizable for each output element.

## why attention?

애초에 attention은 기계 번역 작업에서 대안으로 나왔던 알고리즘이다. 기계 번역 작업의 목표는 A 언어 문장을 B 언어로 자동으로 번역하는 것이다. 초기 기계 번역 모델에서는 전체 소스 문장을 하나의 고정된 context 벡터로 요약하려고 시도했다. 그러니 이 방식은 긴 문장 처리와 번역 품질에 한계가 존재했다.

Attention Mechanism은 인코더의 마지막 숨겨진 상태 하나(last hidden state)로부터 단일 context 벡터를 만드는(seq2seq방식) 대신, 소스 입력 전체와 context 벡터 사이에 지름길 연결을 만드는 것이다. Attention은 이러한 shortcut connection weight를 각 출력 요소(번역의 각 위치에 대한 토큰)에 대해서 커스터마이징 할 수 있도록 한다. 이는 모델이 출력 생성 중에 어떤 부분에 더 집중 해야 하는지를 학습할 수 있게 한다.

context 벡터는 전체 소스 입력 시퀀스에 대해서 접근할 수 있다. 따라서 긴 소스 문장을 처리하는데 있어서 문제가 없으며, 모델은 소스와 대상 간의 정렬을 학습하고 제어한다. 여기서 정렬을 학습한다는 것은 단어 간 상응 관계를 학습한다는 것을 의미한다. 언어마다 문법에 따라 어순과 목적어가 와야 할 위치가 다를 것인데, 언어는 달라도 의미가 같은 문장에서는 요소들이 위치가 다를 수 있다. 그에 대한 학습을 한다는 것이다. 이러한 것에 대한 학습을 하는 과정이 곧 언어를 기계가 학습하는 것으로 볼 수 있다. context 벡터는 여러 정보 소스를 결합하여 출력을 생성하게 된다. context 벡터는 출력 요소마다 업데이트되며, 각 요소에 대한 번역에 대한 정보를 제공한다.

1. Encoder hidden state : 기존 정보
2. Decoder hidden state : 이전 출력 정보
3. 소스와 대상 간의 정렬 정보

![](https://lilianweng.github.io/posts/2018-06-24-attention/encoder-decoder-attention.png)

## Shortcut

shortcut connection은 듣는 순간 떠오르는 논문이 있다. 바로 resnet이다. resnet에서는 deep nn에서 발생하는 gradient lossing 문제를 해결하기 위해 나온 architecture로 굉장히 센세이셔널 했던 구조이다. 지금까지도 많은 architecture들의 backbone으로 사용되기도 할 만큼 그 architecture가 가지는 구조적 강점이 크다. 그 중에서도 중요했던 것이 이 shorcut이다.

Resnet에서의 shortcut은 `Residual connection`이라고도 불린다. 이는 네트워크 레이어를 건너뛰고 입력과 출력을 직접 연결함으로써 gradient가 원활하게 흐를 수 있도록 도왔다.

Attention에서의 shortcut은 인코더와 디코더 사이의 연결을 말한다. 각 출력 요소가 소스 입력의 모든 요소에 대한 sum of weight를 계산하고 이를 사용하여 출력을 생성하는 메커니즘을 설명한다. 이는 모델이 입력과 출력 간에 관계를 학습하는데 사용한다는 점에서 다르다.

## Definition

$\mathbf{x}$는 source sequnece를 나타내고, $\mathbf{y}$는 target sequence를 나타낸다. 각각 n,m의 길이를 가진다. bold체 처리된 것은 vector를 나타낸다는 것을 항상 기억하자.

$$
\mathbf{x} = [x_1,x_2,...,x_n]\\
\mathbf{y} = [y_1,y_2,...,y_m]
$$

**encoder**는 bidirectional rnn이다. forward hidden state는 $\overrightarrow{h_i}$이고, backward hidden state는 $\overleftarrow{h_i}$이다. $i$는 1~n의 범위를 가지는 시간 변수를 나타낸다. encoder는 결국 해당 두 변수를 concatenation한 값이라고 볼 수 있다. (약간의 transpose를 하고...)

$$
\tag{encoder value}h_i = [\overrightarrow{h_i^\intercal}, \overleftarrow{h_i}]^\intercal
$$

**decoder**는 hidden state 값으로 $s_t=f(s_{t-1},y_{t-1},c)$를 가진다. t 시점에서의 context vector c를 넣어주고, 바로 전 시점(t-1)에서의 output word값과 실제 타겟 값 y(t-1)를 넣어준다. 그렇게 함으로써 t시점의 hidden state $s_t$를 계산한다.

기존의 방법론은 모든 hidden state를 계산할 때 동일한 context vector를 사용하는 반면, Bahdanau et al.(2014)은 hidden state를 계산할 때마다 새롭게 만들어진 context vector를 사용하게 된다. 이를 위해 alignment model(score function) $a$를 사용한다.

$$
\begin{align}
c_t =& ~ \displaystyle\sum_{t=1}^n a_{t,i}h_i &\text{Context vector for output y at t}\\
e_{t-1,j} =& ~ a(s_{t-1},h_j) &\text{compare it and attention score calculate}\\
a_{t,i} =& ~ \text{align}(y_t,x_i) &\text{How well two words yt,xi are aligned}\\
=& ~ \frac{\exp(score(s_{t-1},h_i))}{\sum_{i`=1}^n \exp(score(s_{t-1},h_{i`}))} &\text{Softmax of some predefined alignment score}
\end{align}
$$

1. $a$를 이용하여 $s_{t-1}, h_j$가 얼마나 유사한지를 나타내는 attention score $e_{t-1,j}$를 계산한다. 이때 다양한 a의 유형이 사용될 수 있으며 Bahdanau et al.(2014)에서 사용한 것은 아래와 같다

$$
\begin{gather}
a(s_{t-1},h_j) = v_a^T(tanh(W_a[s_{t-1};h_j]))\\
\text{where }v_a, W_a\text{ are learnable parameters}
\end{gather}
$$

2. [softmax](softmax)를 이용해서 attention score를 attention weight(alignment vector) $a_{t-1,j}$로 변환

$$
a_{t-1,j} = \frac{\exp(e_{t-1,j})}{\sum_{k=1}^{T_x}\exp(e_{t-1,j})}
$$

3. 계산된 attention weight와 encoder 부분의 hidden state $h_j$를 가중평균 하여 t시점에 사용될 context vector를 계산한다.

$$
c_t = \displaystyle\sum_{j=1}^{T_x} a_{t-1,j},h_j
$$

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