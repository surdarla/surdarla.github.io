---
layout: post
title: Reducing the Dimemsionality of data with NN
category: 
    - deeplearning
    - paperreview
description: >
    DBN, milestone of Deep learning eve Milestone, show the promise of deep learning
    and the power of neural network.
image: /assets/img/blog/Dimensionality.png
accent_image:
  background: url('/assets/img/blog/Dimensionality.png') center/cover
  overlay: false
accent_color: '#ccc'
theme_color: '#ccc'
invert_sidebar: true
sitemap :
  changefreq : daily
  priority : 1.0
---

* toc
{:toc}

> **[Deep Learning Papers Reading Roadmap 3rd paper]**\
> **[3]** Hinton, Geoffrey E., and Ruslan R. Salakhutdinov. "**Reducing the dimensionality of data with neural networks**." Science 313.5786 (2006): 504-507. [[pdf\]](http://www.cs.toronto.edu/~hinton/science.pdf) **(Milestone, Show the promise of deep learning)** ⭐⭐⭐

## Curse of Dimensionality

우리가 1차원의 데이터를 다루는 것과 10000차원의 데이터를 다루는 것과는 정말 어마어마한 차이가 존재한다는 것이다. 이렇게 차원이 높은 데이터를 다룰 일이 있을까? 하고 약간 막연하게 생각할 수 있지만, 가장 간단한 예로, 100px by 100px 그림은 각각의 픽셀이 하나의 차원이라고 했을 때 10000차원 벡터로 표현이 가능하다. 실제로 머신러닝 분야에서 이미지를 다룰 때는 이런 식으로 처리를 하게 된다. 이 이외에도 high dimensioanl space 상에 존재하는 데이터를 다룰 일은 매우 많이 존재한다.

그렇다면 이런 high dimensional data가 왜 우리가 learning한 system의 성능을 나쁘게 만들까? 정말 간단하게 생각해보자. 만약 우리가 주어진 공간을 regular cell로 나눴다고 가정해보자. 그리고 각각의 cell에 가장 많이 존재하는 class를 그 cell의 class로 생각하여 무조건 그 cell에 존재하는 데이터는 그 class라고 하는 logic을 생각해보자. 당연히 cell의 개수를 무한하게 가져가게 된다면, 그리고 데이터가 무한하다면 이 logic은 반드시 truth로 수렴하게 될 것이다. 이 알고리듬이 제대로 동작하려면 각각의 cell, 혹은 bin이 반드시 차있어야한다. 즉, 비어있는 empty cell이 존재해서는 안된다. 따라서 데이터는 아무리 적어도 cell의 개수만큼은 존재해야한다. 그런데 이렇게 cell을 만들게 될 경우 그 cell의 개수는 dimension이 증가함에 따라 exponential하게 늘어나게 되는 것이다. 예를 들어 우리가 1차원상에서 3개의 bin을 가지고 있다고 하면, 이는 2차원상에서는 9개, 3차원상에서는 27개.. 이렇게 exponentially grow하게 되는 것을 알 수 있다. 이 모델의 parameter들이 exponentially 증가하는 것이다. (아래 슬라이드([출처](http://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)) 참고)

![img](https://sanghyukchun.github.io/images/post/59-2.png)

따라서 당연히 각각의 bin이 비어있지 않도록 ensure해줄 수 있는 data의 개수 역시 exponentially 하게 늘어나게 되고, 즉 차원이 증가하게 되면 필요한 데이터가 exponentailly하게 늘어나게 된다는 것을 의미한다. 그러나 당연히 우리가 3차원 데이터보다 100000차원 데이터를 exponential하게 더 많이 가지고 있으리라는 법은 없고, 이로 인해 문제가 발생하게 되는 것이다.

그리고 또 문제가 되는 것은 high dimensional space에서 정의되는 metric들로, 특히 2-norm 혹은 euclidean distance의 경우는 그 왜곡이 매우 심하여, 실제 멀리 떨어진 데이터보다 별로 멀리 떨어져있지 않고 각 dimension의 방향으로 약간의 noise가 섞여있는 데이터에 더 큰 distance를 부여하는 등의 문제가 존재한다.

조금 다른 예를 들어보자. 만약 D-dimensional space에서 엄청나게 얇은 구각을 만들었다고 생각해보자. 여기에서 ‘구’ 라는 것은 한 점에 대해 거리가 동일하게 떨어져있는 모든 점 내부의 영역을 의미한다는 것은 당연한 것이고.. 이 구의 부피는 $$V_D(r)=K_D r^D$$ 가 될 것이며, $$K_D$$는 그냥 D에 대한 상수라고 생각하면 된다. 그럼 반지름이 1이고 두께가 $$\epsilon$$인 구각의 부피와 반지름이 1인 구의 부피의 비율은 $${V_D(1) - V_D(1-\epsilon) \over V_D(1)} = 1-(1-\epsilon)^D$$ 가 될 것이다. 놀랍게도, 만약 very very high dimension D에서는 이 값이 1로 수렴하게 된다. 즉, 매우 얇은 구각의 부피가 구의 부피와 같다는 의미. 혹은 대부분의 부피가 거의 surface에 가까운 엄청나게 얇은 그 shell에 존재한다는 희한하고 요상한 의미가 된다.

즉, high dimension은 (1) model의 complexity도 증가시키며 (2) 필요한 데이터의 양도 exponentially 하게 늘어나게 하고 (3) 우리가 기존에 사용하던 metric이 제대로 동작하지 않는 그야말로 끔찍한 환경이라 할 수 있다. 그래서 이런 high dimensional space에서 일어나는 여러 문제점들을 통틀어 Curse of dimension이라 한다.

이를 해결하기 위해서는 결국 feature extraction 등의 기술을 사용하여 dimension을 가장 적절하게 낮추는 것이 바람직하다고 할 수 있다.

## Dimensionality Reduction

> It has been obvious that since the 1980s that back propagation through deep autoencoders would be very effective for nonlinear dimensionality reduction, provided that computers were fast enough, data sets were big enough, andthe initial weights were close enough to a good solution.
> Autoencoders give mappings in both directions between the data and code spaces and they can be applied to very large data sets because both the pretraining and the fine-tuning scale linearly in time and space with the number of training cases.

The required gradients are easily obtained by using the chain rule to backpropagate error derivative first through the decoder network and then through the encoder network

If the initial weights are close to a good solution, gradient descent works well, but finding such initial weights requires a very different type of algorithm that learns one layer of features at a time

## Pretrainig procedure

Two-layer networkk called "restricted Boltzmann machine"(RBM) in which stochastic. binary pixels are connected to stochastic, binary feature detectors using symmetrically weighted connections.

$$
E(v,h) = -\sum_{i \in pixels} b_iv_i - \sum_{j\in features}b_jh_j - \sum_{i,j}b_ih_jw_{ij}
$$

aligned test
{:.figcaption}

* Pixel : i
* Feature:j

$$
\Delta w_{ij}=\varepsilon({\lang v_ih_j\rang}_{data} - {\langle v_ih_j\rangle}_{recon})
$$

annotation for aligned math block
{:.figcaption}

* learning rate : $\varepsilon$
* $${\langle v_ih_j\rangle}_{data}$$ : when pixel i and feature detector j  are on together
* $${\langle v_ih_j\rangle}_{recon}$$ : corresponding fraction for confabulations

The first layer of feature detectors then become the visible units for learning the next RBM

adding an extra layer always improves a lower bound on the log probability that the model assigns to the training data, provided the number of feature detectors per layer does not decrease and their weights are initialized correctly

The probability of trainig image can be raised by : Adjusting the weights and biases to lower the energy of that image and to raise the energy of similar, 'confabulated'(created) images that the network would prefer to the real data.

### References

1. [Github implement](https://github.com/nmeripo/Reducing-the-Dimensionality-of-Data-with-Neural-Networks)

### Annotations

[curse of dimension from sanghuckchun]: <https://sanghyukchun.github.io/59/#59-4-cd>
the pixels correspond to 'visible' units of the RBM because their states are observed; the feature detectors correspond to 'hidden' units[^1]

[^1]: something
