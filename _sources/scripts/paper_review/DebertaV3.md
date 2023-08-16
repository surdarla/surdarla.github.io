
# Deberta V3

DEBERTAV3: IMPROVING DEBERTA USING ELECTRA-STYLE PRE-TRAINING WITH GRADIENT-DISENTANGLED EMBEDDING SHARING

Published as a conference paper at ICLR 2023 {bdg-link-primary}`Paper PDF<http://arxiv.org/abs/2111.09543>`

```{admonition} Abstract
:class: dropdown, note

This paper presents a new pre-trained language model, `DeBERTaV3`, which improves the original DeBERTa model by replacing masked language modeling(MLM) with `replaced token detection (RTD)`, a more sample-efﬁcient pre-training task. Our analysis shows that vanilla embedding sharing in ELECTRA hurts training efﬁciency and model performance, because the training losses of the discriminator and the generator pull token embeddings in different directions, creating the “tug-of-war” dynamics. We thus propose a new gradient-disentangled embedding sharing method that avoids the tug-of-war dynamics, improving both training efﬁciency and the quality of the pre-trained model. We have pre-trained DeBERTaV3 using the same settings as DeBERTa to demonstrate its exceptional performance on a wide range of downstream natural language understanding (NLU) tasks. Taking the GLUE benchmark with eight tasks as an example, the DeBERTaV3 Large model achieves a 91.37% average score, which is 1.37% higher than DeBERTa and 1.91% higher than ELECTRA, setting a new state-of-the-art (SOTA) among the models with a similar structure. Furthermore, we have pre-trained a multilingual model mDeBERTaV3 and observed a larger improvement over strong baselines compared to English models. For example, the mDeBERTaV3 Base achieves a 79.8% zero-shot cross-lingual accuracy on XNLI and a 3.6% improvement over XLM-R Base, creating a new SOTA on this benchmark. Our models and code are publicly available at https://github.com/microsoft/DeBERTa.
```

## 문제 설정

PLMs(Pre-trained Language Models)를 scaling up을 해서 파라미터를 수십억 수백만 단위로 늘리는 것이 확실한 성능향상이 있었고 지금까지의 주도적인 방법이었지만, 더 주요한 것은 parameter를 줄이고 computation cost를 줄이는 것이라고 말한다.

Improving Efficency

1. incorporating disentangled attention(imporoved relative-position encoding mechanism)
   - DeBERTA는 1.5B까지 scaling up을 함으로써 SuperGLUE에서 처음으로 사람 performance를 넘어섰다.
1. **Replaced Token Detection(RTD)** vs Masked language modeling(MLM)
   - proposed by ELECTRA(2020)
   - transformer encoder를 오염된 token를 예측하는데 사용하던 BERT(MLM)와는 다르게
   - RTD는 generator, discriminator 를 사용한다. generator는 헤깔리는 오염을 만들어내고, discriminator는 generator가 만든 오염된 토큰을 original inputs과 구분을 해내려한다. 마치 GAN(Generative Adversarial Networks)랑 상당히 비슷한 면이 있다. 차이점에 대해서 분명하게 하자.

여기서 이전의 DeBERTa에서 V3로 나아가면서 바뀐 점으로 두 가지로 꼽는다.
하나는 위에서 말한 BERT의 MLM을 ELECTRA 스타일의 RTD(where the model is trained as a discriminator to predict whethre a token in the corrupt input is either original or replaced by a generator)로 바꾸는 것이고, 다른 하나는 new embedding sharing method이다. ELECTRA에서 generator discriminator는 같은 token embedding을 공유한다.

그러나 연구자들은 본인들의 연구에 따르면 이것은 학습 효율성 면이나 모델의 성능면에서 부정적인 영향을 준다고 말한다. `training losses of the discriminator and the generator pull token embeddings into opposite directions` 즉 생성기와 분류기의 학습의 방향성이 반대이기 때문에 학습 loss가 갈팡질팡할 수 밖에 없다는 것이다. 그럼 생각해볼 수 있는 것이 뒤에 두개의 loss를 만들어서 학습 방향성을 반대로 갈 있도록 했을까 하는 점을 생각해 볼 수 있겠다. token embedding을 달리 준다는 것이 어떤 의미인지 뒤에서 확실하게 나와야 할 것이다. MLM은 generator를 token 중에서 서로 관련이 있어보이는 가까운 것들을 서로 잡아당기면서 학-습을 진행하게 된다. 하지만 반면에 RTD의 discriminator는 의미적으로 가까운 token의 사이를 최대한 멀리하는 방향으로 이진분류 최적화(맞다 아니다)를 하고 pull their embedding을 하게 됨으로써 더욱 구분을 잘 할 수 있도록 하는 것이다. 이러한 '줄다리기 tug-of-war'와 같은 역학이 학습을 망치고, 모델 성능을 떨어트리는 것이라고 말한다. 그렇다고 무조건적으로 seperated embedding을 할 수는 없는 것이 generator의 embedding을 discriminator의 다운스트림 task학습에 포함시키는 것이 도움이 된다고 말하는 논문도 있었기 때문이다.

그래서 그들이 제안하는 것은 `new gradient-disentangled embedding sharing(GDES) method`이다. the generator shares its embeddings with the discriminator but stops the gradients from the discriminator to the generator embeddings. embedding sharing의 장점만을 취하되, 줄다리기 역학은 피할 수 있도록 gradient의 흐름이 discriminator에서 generator로 흐르지는 않도록 하는 방식인 것이다.

### Model Table

| Model                                                                               | Vocabulary(K) | Backbone Parameters(M) | Hidden Size | Layers | Note                                                       |
|-------------------------------------------------------------------------------------|---------------|------------------------|-------------|--------|------------------------------------------------------------|
| **[V2-XXLarge](https://huggingface.co/microsoft/deberta-v2-xxlarge)<sup>1</sup>**   | 128           | 1320                   | 1536        | 48     | 128K new SPM vocab                                         |
| [V2-XLarge](https://huggingface.co/microsoft/deberta-v2-xlarge)                     | 128           | 710                    | 1536        | 24     | 128K new SPM vocab                                         |
| [XLarge](https://huggingface.co/microsoft/deberta-xlarge)                           | 50            | 700                    | 1024        | 48     | Same vocab as RoBERTa                                      |
| [Large](https://huggingface.co/microsoft/deberta-large)                             | 50            | 350                    | 1024        | 24     | Same vocab as RoBERTa                                      |
| [Base](https://huggingface.co/microsoft/deberta-base)                               | 50            | 100                    | 768         | 12     | Same vocab as RoBERTa                                      |
| [DeBERTa-V3-Large](https://huggingface.co/microsoft/deberta-v3-large)<sup>2</sup>   | 128           | 304                    | 1024        | 24     | 128K new SPM vocab                                         |
| [DeBERTa-V3-Base](https://huggingface.co/microsoft/deberta-v3-base)<sup>2</sup>     | 128           | 86                     | 768         | 12     | 128K new SPM vocab                                         |
| [DeBERTa-V3-Small](https://huggingface.co/microsoft/deberta-v3-small)<sup>2</sup>   | 128           | 44                     | 768         | 6      | 128K new SPM vocab                                         |
| [DeBERTa-V3-XSmall](https://huggingface.co/microsoft/deberta-v3-xsmall)<sup>2</sup> | 128           | 22                     | 384         | 12     | 128K new SPM vocab                                         |
| [mDeBERTa-V3-Base](https://huggingface.co/microsoft/mdeberta-v3-base)<sup>2</sup>   | 250           | 86                     | 768         | 12     | 250K new SPM vocab, multi-lingual model with 102 languages |

> 참조
>
> 1. This is the model(89.9) that surpassed T5 11B(89.3) and human performance(89.8) on SuperGLUE for the first time. 128K new SPM vocab.
> 2. These V3 DeBERTa models are deberta models pre-trained with ELECTRA-style objective plus gradient-disentangled embedding sharing which significantly improves the model efficiency.

## Background

### 1. Transformer

Transformer 기반 언어모델들은 $L$개의 transformer block이 쌓여진 형태로 구성된다. 각 블락들은 multi-head self-attention layer들을 포함하고 그 뒤로은 fully-connected positional feed-forward network가 뒤따른다. 기존의 self-attention 메커니즘은 단어의 위치 정보를 encode하는데는 적합하지 않았다. 그래서 기존의 접근법들은 positional bias를 각 input word embedding에 더함으로써, content와 position에 따라서 값이 달라지는 vector로 표현하려고 하였다. 이 positional bias는 absolute position embedding, relative position embedding 등이 있었다. 상대적 위치 임베딩이 좋은 결과들을 최근까지는 보여주고 있는 추세라고 한다.

### 2. DeBERTa

BERT로부터 두 가지 개선점을 보여준다. 우선 DA(Disentengled Attention : 분리된 어텐션), 그리고 enhanced mask decoder이다. 이전의 single vector로 하나의 input word의 내용과 위지정보를 표현하려는 것과는 다른게, DA는 두 개의 seperate vector를 사용한다. `one for the content and one for the position`. 그러면서 DA 메커니즘의 단어들 사이의 attention weight는 disentangled matrices에 의해서 계산되고 이는 각각 내용과 상대적 위치 두 개가 각각의 행렬로 다르게 계산된다.

그리고 MLM에 대해서는 BERT와 동일하게 사용된다. DA가 이미 내용과 상대적 위치에 대한 고민이 들어가는 있지만, 중요한 것은 absolute position에 대한 고민은 없다. absolute position은 예측에서 꽤나 주요한 요소임으로 이러한 점을 보완하기 위해서 DeBERTa에서는 enhanced Mask Decoder를 MLM을 보완하기 위해서 사용한다. 이는 MLM decoding layer에서 context word에 absolute position information이 추가로 들어가는 방식이다.

### 3. ELECTRA

#### 2.3.1 Masked Language Model(MLM)

Large-scale Transformer-based PLMs 는 보통 많은 양의 텍스트로 사전학습되면서 self-supervision objective(자기주도학습의 목적)인 MLM을 실현하고 이 말인 즉슨 문맥을 이해하게 된다는 것이다.

$X = \{x_i\}$는 하나의 sequence이고 $\tilde{X}$는 15%의 토큰이 오염(masking)된 것이다. 목표는 다시 reconstruct $X$이다. 방법은 language model을 predicting the masked tokens $\tilde{x} \text{ conditioned on } \tilde{X}$ 하면서 훈련시키는 것이고 parameterized by $\theta$이다.

$$
\max_{\theta}\log p_{\theta}(X|\tilde{X}) = \max_{\theta}\sum_{i\in C} \log p_{\theta}(\tilde{x}_i|\tilde{X})
$$

C : index set of the masked tokens in the sequence\
BERT에서는 10%의 masked tokens를 바꾼 상태로 유지하고, 다른 10%의 무작위 선택된 토큰을 바꾸었고, 나머지 80%는 아예 $[MASK]$ token으로 유지했다.

#### 2.3.2 Replaced Token Detection(RTD)

BERT는 하나의 transformer encoder를 사용했고, MLM으로 훈련되었다. 이와 다르게 ELECTRA는 두 개의 transformer encoders를 사용하면서 GAN처럼 훈련했다. Generator encoder는 MLM으로 훈련되었고, discriminator encoder는 `token-level binary classifier`로 훈련되었다. generator는 input sequence에서 마스킹된 token을 대체할 ambiguous한 토큰을 생성했다. 그리고 이렇게 만들어진 sequence는 dicriminator로 들어가서 해당 토큰이 original 토큰이 맞는지 아니면 generator가 만든 토큰인지를 이진 분류한다. 그리고 이 이진분류하는 것이 RTD이다. 여기서 parameterized 되는 부분이 $\theta_{G}$는 generator의 파라미터이고, $\theta_{D}$는 discriminator의 파라미터이다. Loss function of the generator는 아래와 같다.

$$
L_{MLM} = \mathbb{E} \Big(-\sum_{i \in C}\log p_{\theta_G} \big(\tilde{x}_{i,G} = x_i|\tilde{X}_G \big) \Big)
$$

- $p_{\theta_G} \big(\tilde{x}_{i,G} = x_i|\tilde{X}_G \big) \Big)$ : 이 부분이 G가 $\tilde{X}_G$를 $x_i$로 재구성할 확률이다.
- 특히나 masking된 token($\tilde{X}_G$)은 원본에서 randomly masking한 15%이다.

```{admonition} Log의 성질
:class: dropdown, note

- log앞에 붙은 - 는 재구성할 확률이 높아질수록 generator가 일을 잘하는 것이기 때문에, 위의 재구성할 확률이 높아질수록 loss값은 낮아지는 구성이 되어야 모델이 목표함수에 의거한 학습을 진행하기에 붙은 것이다.
- log는 0~1사이의 확률값$\mathbb{E}$을 0~$\infty$ 값으로 변환한다. 이를 통해서 underflow(0 * 0 * ... -> 0에 점점더 가까워지는)를 방지하며, 곱셈을 덧셈으로 변환하는 성질을 이용한다.
```

discriminator에 들어가는 input sequences는 generator의 output probability에 따라서 new tokens이 masked tokens 자리를 채운채로 들어온다. 그래서 i가 C안에 없으면 그대로 x이고(replaced token이 아니라 아예 원본이기 때문), index가 C에 있는거만 비교를한다.

$$
\tilde{x}_{i,D} =
\begin{cases}
\tilde{x}_i \sim p_{\theta_G} \big(&\tilde{x}_{i,G} = x_i|\tilde{X}_G\big), & i\in C    \\
& x_i, &i\notin C
\end{cases}
$$

- $\sim$ : sim 기호는 'distributed as' 또는 'has a distribution of'로 해석되며, '특정 확률 분포를 따른다는 의미', '따른다, 분포한다'입니다. 여기서 sim 기호는 주어진 확률 분포 $p_{\theta_G}$에 따라 변수 $\tilde{x}_i$가 분포한다는 것을 의미.
- 따라서, $\tilde{x}_i \sim p{\theta_G} (\tilde{x}_{i,G} = x_i|\tilde{X}_G)$는 변수 $\tilde{x}_i$가 조건부 확률 분포 $p{\theta_G} (\tilde{x}_{i,G} = x_i|\tilde{X}_G)$를 따른다는 것을 의미합니다. 이 분포는 $p_{\theta_G}$ 파라미터를 가지며, $\tilde{X}_G$가 주어졌을 때 $\tilde{x}_{i,G} = x_i$인 조건부 분포를 나타냅니다. 위 수식의 전체적인 의미는, 인덱스 i가 집합 C에 포함되어 있으면, $\tilde{x}_i$는 조건부 분포 $p_{\theta_G} (\tilde{x}_{i,G} = x_i|\tilde{X}_G)$를 따르고, 그렇지 않으면 $\tilde{x}_i$는 $x_i$와 동일하다는 것을 의미합니다.

$$
L_{RTD} = \mathbb{E}\Big( -\sum_{i}\log p_{\theta_D} \big(\mathbb{I}(\tilde{x_{i,D}} = x_i)|\tilde{X}_D,i   \big)  \Big)
$$

- $\mathbb{I}$ : indicator function을 말한다. $(\tilde{x_{i,D}} = x_i)$를 충족하면 1을 반환하고, 아니면($\tilde{X}_D,i$) 0을 반환하는 함수를 말한다. 매우 엄격한 함수로 볼 수 있으며 후보는 'sigmoid', 'tahn', 'ReLU', 'Leaky ReLU'등이 있다.
- 위 discriminator의 loss function의 input은 $\tilde{X_D}$ 이며 이것은 위의 3번 equation의 result이다. 즉 discriminator에서 한번 걸러져 나온 것이 loss function에 들어가는 것이다.

총체적인 ELECTRA의 loss function은 아래와 같이 정리할 수 있다.
$$
L = L_{MLM} + \lambda L_{RTD}
$$

- $\lambda$ : discriminator loss function에 대한 weight를 나타냄. 모델 학습에서 해당 손실의 중요성을 조절하는데 사용됨. 여기서는 50임으로 MLM에 비해서 50배의 가중치를 더 곱해준다는 의미임으로 RTD에 엄청 중요성을 높게 쳐주는 것이라고 볼 수 있다.

## DeBERTaV3

DeBERTa + RTD training loss + new weight-sharing method

### 3.1 DeBERTa + RTD

ELECTRA에서 가져온 RTD, 그리고 DeBERTa disentangled attention mechanism의 합은 프리트레이닝 과정에서 간단하고 효과적인 것으로 판별되었다. 이전 DeBERTa에서 사용되었던 MLM objective를 RTD objective로 바꿈으로써 더욱 disentangled attention mechainsm을 더욱 강화하는 것이다.

training 데이터로는 Wikipedia, bookcorpus의 데이터가 사용되었다. generator는 discriminator와 같은 width를 가지되 depth는 절반만 가져간다. batch size는 2048이며 125,000 step이 훈련되었다. learning_rate = 5e-4, warmup_steps = 10,000, 그리고 위에서 말했듯이 RTD loss function에 가중치를 50을 줌으로서 optimization hyperparameter를 사용하였다.

검증 데이터로는 MNLI, SQuAD v2.0을 사용하였고, 이 데이터들에 대한 정리도 필요할 것이다. 결과적으로 DeBERTa를 압도하지만 더욱더 improved될 있는 포인트를 말하는 지점이 있다. token Embedding Sharing(ES) used for RTD(기존에 사용되었던)를 new Gradient-Disentangled Embedding Sharing(GDES) method로 바꿈으로써 더욱 발전될 가능성이 있다고 말한다.

### 3.2 Token Embedding Sharing (in ELECTRA)

ELECTRA에서는 generator와 discriminator가 token embedding을 공유한다. 이것이 `Embedding Sharing(ES)`이다. 이 방법은 generator가 discriminator에 input으로 들어갈 정보를 제공함으로써 학습에 필요한 parameter를 줄여주는 역할을 하고 학습을 용이하게 해준다. 그러나 앞에서 말했듯이 두 기제의 목적 방향성이 반대이기 때문에 서로를 방해하고, 학습 수렴을 저해할 가능성이 크다.

- $E$ : token embeddings
- $g_E$ : gradients = $\frac{\delta L_{MLM}}{\delta E} + \lambda\frac{\delta L_{RTD}}{\delta E}$

위의 equation은 token embeddings(E)가 두 개의 일에서의 gradient를 한 번에 조정하면서 update된다는 것을 의미한다. 위에서 말했듯이 이것은 줄다리기 이다. 아주 조심스럽게 update 속도를 조절하면서(small learning_rate, gradient clipping) 학습을 진행하면 결론적으로는 수렴을 하기는 한다고 말한다. 하지만 두 개의 task가 정반대의 목적을 가진다면 이것은 굉장히 비효율적이며, 해당 상황(MLM,RTD)은 정확히 그런 상황이라고 볼 수 있다. 두 개의 task가 token embedding을 업데이트 하면서 바라는 것이 하나는 유사성에 따라서 가깝게 하고, 다른 하나는 유사성에 따라서 멀게하여 분류하는 것이기 때문이다.

이것을 실제로 확인하기 위해서 여러 다양한 ELECTRA를 구현하되, 해당 ELECTRA들은 token embedding을 공유하지 않도록 구현했다고한다. 그렇게 구현을 하면 No Embedding Sharing(NES)가 되는 것이다. 얘네는 gradient update가 각각 된다. 우선은 (1) generator의 parameter(token embedding with $E_G$)가 MLM loss를 back-prop하면서 업데이트되고, (2) 이후에 discriminator가 generator output을 input으로 받는다 (3) 마지막으로 discriminator parameter(token embeddings with $E_D$)를 RTD loss를 back-prop하면서 update한다.

이들은 3가지로 ES vs NES를 비교했다고 한다.

1. convergence speed : NES가 당연히 gradient conflict를 방지함으로 승리
2. quality of token embeddings : average cosine similiarity scores를 비교했다. $E_G$에서는 굉장히 효과가 좋았지만 $E_D$는 학습을 거의 못한 것으로 보였다. 효과가 좋다는 것은 의미적으로 coherent 일관성 있게 $E_G$가 코사인 유사도가 매우 높아지는 것을 말한다.
3. performance on downstream NLP tasks : 또한 NES가 다운스트림 test에서도 좋은 모습을 보이지 못했다

> ES가 generator embedding으로부터 discriminator가 학습을 할 때 도움을 받는게 장점이 있다는 것을 알 수 있다.

### ???? average cosine similiarity of word embeddings of the G vs D

average cosine similiarity가 높을수록 좋은 것인가?
어떤 의미인지 제대로 이해를 못한 거 같다.

### 3.3 Gradient-Disentangled Embedding Sharing(GDES)

ES, NES의 단점을 꽤 뚫기 위해 해당 논문에서 중요하게 말하는 지점이다. 두 개의 장 단점이 분명하게 존재하면서 두 개를 모두 챙길 방법으로 나온 것이다. 한 번 정리를 하자면 ES는 학습은 느리지만 generator output : token embedding를 discriminator가 참조하면서 학습 parameter reducing에 도움을 받는 다는 것이다. 하지만 단점은 generator discriminator token embeddings가 둘 다 일관성이 없어진다는 것이다.

반면에 NES는 학습이 굉장히 빨라진다. G,D의 방향성의 정반대의 성질을 해결해 줌으로써 학습이 용이하게 된다고 볼 수 있다. 하지만 결론적으로는 학습을 오히려 ES보다 못한 꼴이 난다. 그래도 장점은 G의 token embedding이 코사인 유사도가 높은 일관성 있는 embedding을 만들어주는 경향성을 만드는 것이 가능하다고 볼 수 있다.

이 모든 단점을 커버하고 도대체 어떻게 장점만 남긴다는 것인가? 장점만 남긴다면 학습의 속도도 빨라지면서 동시에 G,D의 token embedding이 유사성을 유지하는 것이 될 것이다. 후자를 논문에서는 'learn from same vocabulary and leverage the rich semantic information encoded in the embeddings'라고 말한다.

이것을 GDES는 오직 generator embeddings를 MLL loss만 가지고 업데이트함으로써, output의 일관성과 통일성을 유지한다. 그것을 수식적으로 보면

$$
E_D = sg(E_G) + E_{\Delta}
$$

원래는 NES에서는 $E_D$로 바로 backprop하던 것을 re-parameterize하여 discriminator embedding를 새로 정의한다. $sg$d의 역할은 $E_G$에서 나온 gradient가 계속 흘러들어가는 것을 막고, residual embeddings $E_{\Delta}$ 만을 업데이트 하게 하는 것이다. 이것은 residual learning에서의 아이디어와 굉장히 유사한 것 같은데!!!.

(1) G output -> input for discriminator = $E_G$\
(2) update $E_G$ $E_D$ with MLM loss\
(3) D run on G output\
(4) update $E_D$ with RTD loss with only $E_{\Delta}$\
(5) after training, $E_{\Delta}$ + $E_G$ = $E_D$

> 셋은 embedding sharing의 차이만 있고, computation cost의 차이는 없으다.
> computation cost의 차이가 없이 아이디어만으로 성능의 up을 한 것도 resnet이랑 비슷하다.

코사인 평균 유사도에서도 차이가 NES보다는 덜한데 이는 'preserves more semantic information in the discriminator embeddings through the partial weight sharging'이라고 말한다. 여기서 보이는 partial weight sharing이 $E_{\Delta}$이며 이것이 embedding의 잔차를 학습하는 방식으로 진행됨으로써 학습을 용이하게 가져갔다... 정도로 보인다.

## Conclusion

- pre-training paradigm for language models based on the combination of DeBERTa and ELECTRA, two state-of-the-art models that use relative position encoding and replaced token detection (RTD) respectively
- interference issue between the generator and the discriminator in the RTD framework which is well known as the “tug-of-war” dynamics.
- GDES : the discriminator to leverage the semantic information encoded in the generator’s embedding layer without interfering with the generator’s gradients and thus improves the pre-training efﬁciency
- a new way of sharing information between the generator and the discriminator in the RTD framework, which can be easily applied to other RTD-based language models
- debertav3-large : 1.37% on the GLUE average score
- 목적 : `parameter-efﬁcient pre-trained language models`

## Reference

1. [kpmg notion - Deberta Review](https://kpmgkr.notion.site/DeBERTa-421579f197f840f48cc920f09cbbb70b)
2. [HF - lighthouse/mdeberta-v3-base-kor-further](https://huggingface.co/lighthouse/mdeberta-v3-base-kor-further)
3. [github - microsoft/DeBERTa](https://github.com/microsoft/DeBERTa)
