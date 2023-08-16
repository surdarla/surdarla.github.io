# DeBERTa

DEBERTA: DECODING-ENHANCED BERT WITH DIS-ENTANGLED ATTENTION

Published as a conference paper at ICLR 2023 {bdg-link-primary}`Paper PDF<https://arxiv.org/pdf/2006.03654>`

Pengcheng He, Microsoft Dynamics 365 AI\
Xiaodong Liu, Microsoft Research\
Jianfeng Gao, Microsoft Research\
Weizhu Chen, Microsoft Dynamics 365 AI\
{penhe,xiaodl,jfgao,wzchen}@microsoft.com

microsoft에서 deberta를 만들었다보니 집필진이 전부 microsoft이다.

```{admonition} Abstract
:class: dropdown, note

Recent progress in pre-trained neural language models has significantly improved the performance of many natural language processing (NLP) tasks. In this paper we propose a new model architecture DeBERTa (Decoding-enhanced BERT with disentangled attention) that improves the BERT and RoBERTa models using two novel techniques. The first is **the disentangled attention mechanism**, where each word is represented using two vectors that encode its content and position, respectively, and the attention weights among words are computed using disentangled matrices on their contents and relative positions, respectively. Second, an **enhanced mask decoder** is used to incorporate absolute positions in the decoding layer to predict the masked tokens in model pre-training. In addition, a **new virtual adversarial training method** is used for fine-tuning to improve models' generalization. We show that these techniques significantly improve the efficiency of model pre-training and the performance of both natural language understanding (NLU) and natural langauge generation (NLG) downstream tasks. Compared to RoBERTa-Large, a DeBERTa model trained on half of the training data performs consistently better on a wide range of NLP tasks, achieving improvements on MNLI by +0.9% (90.2% vs. 91.1%), on SQuAD v2.0 by +2.3% (88.4% vs. 90.7%) and RACE by +3.6% (83.2% vs. 86.8%). Notably, we scale up DeBERTa by training a larger version that consists of 48 Transform layers with 1.5 billion parameters. The significant performance boost makes the single DeBERTa model surpass the human performance on the SuperGLUE benchmark (Wang et al., 2019a) for the first time in terms of macro-average score (89.9 versus 89.8), and the ensemble DeBERTa model sits atop the SuperGLUE leaderboard as of January 6, 2021, out performing the human baseline by a decent margin (90.3 versus 89.8).
```

## 문제 설정 Introduction

Transformer는 nlp에서 가장 효과적인 network architecture로 자리잡았다. 순서에 따라 text를 처리하는 RNN들과 다르게, tranformers는 입력 텍스트(input text)의 모든 단어(every words)에 대해서 self-attention을 적용하여, attention weight를 뽑아낸다. 그리고 이 attention weight는 각 단어들이 서로에게 어떠한 영향을 미치는지를 나타내는 수치이다. 이러한 방식(병렬처리)을 transformer가 사용하고 있기 때문에 RNN과 같은 순차처리 모델보다 large-scale training이 가능한 것이다.

### 1.1 Parallelization

RNN과 transformer는 둘 다 sequence modeling architecture이다. 하지만 transformer는 시퀀스의 모든 위치에 대해 동시에 연산을 수행해서 병렬화가 더 쉽다. 병렬화라는 말 자체는 하나의 작업을 여러 개의 작은 자겅ㅂ으로 나누어 동시에 처리함으로써 전체적으로는 하나의 작업을 더 빠르고 효율적으로 수행하는 기술을 말한다. 딥러닝 모델의 학습은 계산량, 데이터량이 많을 수록 좋은 방향으로 흘러가고 있기 때문에 이러한 기술은 필수적이다. GPU를 동시에 사용하거나 데이터를 쪼개거나, 연산을 쪼개거나 하는 방식으로 여러 부분에서 쪼개어 동시다발적으로 수행하는 것을 전반적으로 병렬화라고 말할 수 있다.

병렬화를 가능하게 하는 3가지 특징은 다음과 같다.

1. Attention 메커니즘: Transformer는 Self-Attention 메커니즘을 사용하여 입력 시퀀스의 모든 요소를 동시에 처리할 수 있습니다. 이로 인해 서로 독립적인 계산이 가능하며, 병렬 처리에 적합합니다.
2. Layer 단위 병렬화: Transformer의 인코더와 디코더는 여러 층으로 구성되어 있으며, 이러한 층들은 독립적으로 병렬로 계산할 수 있습니다.
3. 마스킹: 학습 시에는 한 번에 하나의 출력만을 생성하도록 마스킹하여 순차적으로 계산할 수도 있습니다. 하지만 추론(inference) 단계에서는 병렬화하여 동시에 여러 개의 출력을 생성할 수 있습니다.

### 1.2 Disentangled attention

> relative position embedding를 사용하자. 근데 vector를 두 개로 나눠서..

**기존의 self-attention의 위치정도 encoding 문제**\
원래(transformers)의 self-attention mechanism은 주어진 input sequence에서 모든 위치의 정보를 사용하여 output을 생성한다. input sequence의 모든 위치 간의 관계를 높은 수준의 상호의존성을 가진 전연결 그래프로 모델링을 하기 때문에, sequence의 길이가 길어질수록 연산량이 증가하고, 장기의존성을 학습하는데 어려움이 커진다.

**positional bias**\
때문에 기존의 word embedding에 positional bias를 추가해줘서 하나의 벡터에서 content와 position의 정보를 포함하도록 하는 방식이 사용되었다.

- absolute position embedding : 문장 내 위치만 고려
- relative position embedding : 단어간 상대적 위치만 고려

기존 BERT를 본 논문에서는 이렇게 말한다. `each word in the input layer is represented using **a vector** which is the sum of its word (content) embedding and (absolute)position embedding`. 분명하게 absolute position 정보가 중요한 것은 맞지만 뒤에서 따른 방법으로 이용하되, 여기서는 relative position embedding을 이용하여 위치정보를 input으로 사용하고, 실제로 많은 선제연구들에서 이 방법의 중요성을 말해줬다고 한다.

| ..          | word in input layer                         |
| :-----------: | :-------------------------------------------: |
| transformer | word itself                                 |
| Bert        | vector(word embedding(token) + position embedding) |
| Deberta     | vector(word embedding(token)),vector(absoulte position embedding) |

**여기서는 relative word embedding을 사용**\
disentangled attention은 이렇게 각각의 embedding으로 word에 대한 표현을 한 뒤, 각각의 attention weight를 `disentangled matrices = 2개의 vectors -> 2x2 = 4개의 matrices`를 이용해서 계산한다. 이는 단어의 관계라는 것이 의미적 관계만 있는 것이 아니라 상대적인 위치에 의해서도 영향을 받는 것에서 나온 것이다. 본문의 예시는 'deep','learning'이라는 두 단어가 다른 문장에서 있을 때보다 옆에 붙어있을 때 의존성이 굉장히 높아지는 것으로 든다.

### 1.3 Enhanced mask decoder

absolute position embedding 더하기

MLM : masked language modeling은 Bert에서 나왔던 것으로 해당 모델 역시 이 방법을 사용해서 기본적인 pre-training을 진행한다. MLM 이라는 것은 `fill-in-the-black task`로 주변의 단어들을 사용해서 blank(masked word)의 원래 word를 유추해 내는 것이고, deberta의 차이는 MLM을 하되 위의 disentangled 어텐션을 사용해서 두 개의 별개의 vector를 이용해서 MLM을 수행한다. 문제는 position embedding이 상대적인 위치를 사용하지만 단어의 절대적 위치가 없다는 것이다. 절대적 위치는 구문론적으로 이해를 돕는 굉장히 중요한 정보라고 말한다.

> a new store opened beside the new mall

이러한 예시에서 store, mall이 둘 다 masking되었을때, 둘의 context적인 의미는 '가게'로 비슷하지만 구문론적으로 앞의 store는 주어의 역할을 하고 있다. 이러한 구문론적인 정보를 주는 것은 context, content가 아니라 absolute position이다.

해서 deberta에서는 이러한 absolute position embedding을 softmax layer 직전에 넣어준다. 바로 이 지점이 모델이 앞에서 말한 content, position embedding 조합을 기반으로 masking을 해독하기 직전이다. 그니깐 거의 마지막에 넣어주는 것으로 '참조'의 수준으로 하는 것으로 보인다.

### 1.3 virtual adversarial training

이건 자세하게 설명이 앞에 안나오는데 model generalization에 좋다고 한다.

### 1.4 MLM

Masked Language Model

기존의 large-scale transformer-based PLM(pretrained language model)들은 보통 많은 양의 텍스트를 가지고 문맥적인 단어의 표현(contextual word representation)을 배우기 위해서 학습 과정을 거쳤다. 이 학습 과정은 'self-supervision objective' 그러니깐 자기지도 학습인데, 방법론 적으로는 MLM을 가리킨다. 이제 수식적으로 들어가보자

```{admonition} MLM
:class: dropdown, note

given a sequence $X = \{x_i\}$\
corrupt it into $\tilde{X}$ by 15% of its tokens at random\
model parameterized by $\theta$\
train model to reconstruct $\tilde{X}$\
by predicting the masked token $\tilde{x}$ conditioned on $\tilde{X}$

$$
\max_{\theta}\log p_{\theta}(X|\tilde{X}) = \max_{\theta} \sum_{i\in C} \log p_{\theta}(x_i = x_i | \tilde{X})
$$

- C = index set of the masked tokens in sequence
- 10%의 masked tokens는 변치않은 대로 두고
- 다른 10%는 무작위로 고른 것과 바꾸고
- 80%는 mask token으로 바꾸라고 한다.

```

## DeBERTa architecture

### 3.1 Disentangled attention

a two-vector approach to content and position embedding

> $i$ : position of token in a sequence\
> $\{H_i\}$ : content of token, hidden state, output from encoding\
> $\{P_{i|j}\}$ : relative position with j-th token, from distance of tokens\

**cross attention score token_i / token_j**

$$
\begin{matrix}
A_{i,j} &=& \{H_i,P_{i|j}\} \times \{H_i,P_{j|i}\}^{\intercal}\\
        &=& H_iH_j^{\intercal} + H_iP_{j|i}^{\intercal} + P_{i|j}H_j^{\intercal}+P_{i|j}P_{j|i}^{\intercal}\\
\end{matrix}
$$

하나의 단어 쌍에 대해서 attention weight를 계산하려면 4 attention score를 구해야 한다. 이 과정에서 사용되는 것이 `disentangled matrices`이고 이는 content position 두 개에 대해서 `content-content`,`content-position`,`position-content`,`position-position`로 4개가 된다.

  1. $H_i H_j^{\intercal}$: i번째 토큰의 내용 정보와 j번째 토큰의 내용 정보 간의 상호작용을 나타냅니다. 이는 토큰 간의 내용적인 유사성을 측정합니다.`content-content`
  2. $H_i P_{j|i}^{\intercal}$: i번째 토큰의 내용 정보와 j번째 토큰에 대한 i번째 토큰의 상대적 위치 정보 간의 상호작용을 나타냅니다. 이는 i번째 토큰의 내용이 j번째 토큰에 대한 위치에 어떻게 영향을 미치는지를 측정합니다.`content-position`
  3. $P_{i|j} H_j^{\intercal}$: i번째 토큰에 대한 j번째 토큰의 상대적 위치 정보와 j번째 토큰의 내용 정보 간의 상호작용을 나타냅니다. 이는 j번째 토큰의 내용이 i번째 토큰에 대한 위치에 어떻게 영향을 미치는지를 측정합니다.`position-content`
  4. $P_{i|j} P_{j|i}^{\intercal}$: i번째 토큰에 대한 j번째 토큰의 상대적 위치 정보와 j번째 토큰에 대한 i번째 토큰의 상대적 위치 정보 간의 상호작용을 나타냅니다. 이는 토큰 간의 상대적인 위치적 유사성을 측정합니다.`position-position - relative position embedding에서는 제거되는 부분`

**이 4개를 disentangled attentions라고 하는 것이다**\
이전의 relative position encoding은 기존의 attention weight에다가 relative position bias를 더해주는 식으로 위에서의 1,2번만을 사용하는 식으로 사용되었다. 하지만 deberta에서는 이렇게 모든 것을 사용하되 4번은 안사용한다. 이미 1,2,3에서 두 토큰 간의 상대적 위치 정보를 충분히 capture한다고 판단했기 때문에 수식상으로는 out되었다고 한다.

### 3.1.1 standard self-attention operation

> $R^{N \times d}$ : N(문장의 길이, 토큰의 수)개의 행 * d(토큰의 hidden 벡터의 차원)개의 열 - 차원의 실수(R) 행렬\
> $H \in R^{N \times d}$ : input hidden vectors\
> $H_o \in R^{N \times d}$ : output of self-attention\
> $W_q,W_k,W_v \in R^{d \times d}$ : projection matrices\
> $A \in R^{N \times N}$ : attention matrix

$$
\begin{matrix}
Q &=& HW_q,\\
K &=& HW_K,\\
V &=& HW_v,\\
A &=& \frac{QK^T}{\sqrt{d}}\\
H_o &=& \text{softmax}(A)V\\
\end{matrix}
$$

여기서 Q, K, V는 각각 query, key, value를 나타내며, d_k는 key의 차원을 나타냅니다. 이 때 각 토큰의 위치 정보는 absolute positional encoding 방식을 통해 각 토큰의 hidden state에 추가되고, 이 정보가 포함된 hidden state가 query, key, value로 사용됩니다.

### 3.1.2 relative distance

> $k$ : maximum relative distance\
> $\delta(i,j)\in[0,2k)$ : the relative distance from token i to token j

$$
\delta(i,j) =
\begin{cases}
0 & \text{for} & i-j\leqslant-k\\
2k-1 & \text{for} & i-j\geqslant k\\
i-j+k &\text{others.} &\\
\end{cases}
$$

여기서 [ : 포함, ) : 미포함을 의미한다. 상대적 거리값이 0<=x<2k 의 뜻이라고 한다. 0~2k-1사이의 정수 값

### 3.1.3 disentangled self-attention

with relative position bias as equation 4
> $Q_c,K_c,V_c$ : projected content vectors from projection matrices\
> $W_{q,c},W_{k,c},W_{v,c} \in R^{d\times d}$ : projection matrices\
> $P \in R^{2k\times d}$ : relative position embedding vectors shared with all layers\
> $Q_r, K_r$ : projected relative position vectors\
> $W_{q,r},W_{k,r} \in R^{d\times d}$ : projection matrices

$$
\begin{matrix}
Q_c &=& HW_{q,c},\\
K_c &=& HW_{k,c},\\
V_c &=& HW_{v,c},\\
Q_r &=& PW_{q,r},\\
K_r &=& PW_{k,r}\\
\end{matrix}
$$

> $\tilde{A}_{i,j}$ : $\tilde{A}$의 요소. 토큰 i에서 token j 로의 어텐션 스코어\
> $Q_i^c$ : i-th row of $Q_c$\
> $Q^r_{\delta(j,i)}$ : $Q_r$ with regarding to 상대적 거리 $\delta(j,i)$

$$
\tilde{A}_{i,j} = Q_i^cK_j^{c\intercal} + Q_i^c{K_{\delta(i,j)}^r}^\intercal + K_j^c{Q_{\delta(j,i)^r}}^\intercal
$$

### projection matrix

한 벡터나 공간을 다른 공간으로 mapping하는 것을 도우는 matrix

