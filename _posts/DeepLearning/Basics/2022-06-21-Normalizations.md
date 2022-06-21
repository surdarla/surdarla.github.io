---
layout: post
title: Basic normalizations for deep learning
category: 
    - deeplearning
    - basics
description: >
  Normalization 정리
image: /assets/img/blog/basics/normalization.png
accent_image:
  background: url('/assets/img/blog/basics/normalization.png') center/cover
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
## Why normalization?

딥러닝에서 unbounded한 activation functions(ReLU, ELU)들 때문에 normalization은 중요하게 된다. 이러한 activation function은 output이 (tanh이 [-1,1] 사이로 만들어준다면) 규제되지 않기 때문에, 학습이 진행될 수록 값이 무한한하게 커질 수 있기 때문에 normalization을 사용하는 것이다. ReLU 자체가 gradient vanishing 문제를 해결하기 위해서 (softmax [0,1], tanh[-1,1] 사이로 값을 규제) 나왔지만, 0이 아닌 값을 그대로 내보내기 때문에 이 부분에 대해서 normalize 하는 것이 학습에 더욱 도움이 된다는 결과 들이 있었기 때문에 normalization $$\to$$ activation function 순으로 사용하고 있다.

그중에서 AlexNet[^1]에서 처음 나왔던 Local response normalization을 시작으로 이에 대한 정리를 한다.

### LRN : Local Response Normalization

신경망은 기본적으로 인간의 neuron을 모방한 구조이다. 뉴런의 기전중에 *lateral inhibition(측면억제)*이라는 것이 있는데 이는 'the capacity of a neuron to reduce the activity of its neighbors', 즉 한 영역에 있는 신경 세포가 상호 간 연결되어 있을 때 한 그 자신의 축색이나 자신과 이웃 신경세포를 매개하는 중간신경세포(interneuron)를 통해 **이웃에 있는 신경 세포를 억제하려는 경향**이다.[^2] DNN에서는 지역적으로 가장 최대값을 가지는 pixel의 정보를 다음 Layer에 전달하는 것이 중요하기 때문에 activation function에서 이러한 측면억제의 역할을 하는 부분이 필요하다.

![LRN 2types](https://miro.medium.com/max/700/1*MFl0tPjwvc49HirAJZPhEA.png)
2types of LRN
{:.figcaption}

- Non-trainable layer

- 2 타입
  - Inter-Channel LRN



$$
\begin{align*}
	b_{x,y}^i = a_{x,y}^i / \big(k + a\sum_{j=\max(0,i-n/2)}^{\min(N-1,i+n/2)}(a_{x,y}^j)^2 \big)^\beta
\end{align*}
$$

**The neighborhood defined is across the channel**

$$i$$ : output of the filter i

a(x,y) : the pixel values at (x,y) position before normalization

b(x,y) : the pixel values at (x,y) position after normalization

k : used to avoid any singularities - division by zero

a : normalization constant

$$\beta$$ : contrasting constant

n : define the neighborhood length

$$(k,a,\beta,n) = (0,1,1,N)$$ : standard normalization

- Intra-Channel LRN


$$
b_{x,y}^i = a_{x,y}^i / \big(k + a\sum_{i=\max(0,x-n/2)}^{\min(W,x+n/2)}\sum_{j=\max(0,y-n/2)}^{\min(W,x+n/2)}(a_{x,y}^j)^2 \big)^\beta
$$

**The same channels only**



## Batch normalization





- 

## References

- [Medium-normalizations](https://towardsdatascience.com/difference-between-local-response-normalization-and-batch-normalization-272308c034ac)

- [^1]: [Imagenet Classification with Deep Convolutional Neural Network:AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

- [^2]: [lateral inhibition explanation in wiki](https://ko.wikipedia.org/wiki/%EC%B8%A1%EB%A9%B4_%EC%96%B5%EC%A0%9C#:~:text=%EC%8B%A0%EA%B2%BD%EC%84%B8%ED%8F%AC%EB%93%A4%EC%9D%B4%20%ED%9D%A5%EB%B6%84%ED%95%98%EA%B2%8C%20%EB%90%98%EB%A9%B4%20%EC%98%86%EC%97%90%20%EC%9E%88%EB%8A%94%20%EC%9D%B4%EC%9B%83%20%EC%8B%A0%EA%B2%BD%EC%84%B8%ED%8F%AC%EC%97%90%20%EC%96%B5%EC%A0%9C%EC%84%B1%20%EC%8B%A0%EA%B2%BD%EC%A0%84%EB%8B%AC%EB%AC%BC%EC%A7%88%EC%9D%84%20%EC%A0%84%EB%8B%AC%ED%95%98%EC%97%AC%2C%20%EC%9D%B4%EC%9B%83%20%EC%8B%A0%EA%B2%BD%20%EC%84%B8%ED%8F%AC%EA%B0%80%20%EB%8D%9C%20%ED%99%9C%EC%84%B1%ED%99%94%EB%90%98%EB%8F%84%EB%A1%9D%20%EB%A7%8C%EB%93%9C%EB%8A%94%20%EA%B2%83%EC%9D%B4%EB%8B%A4)

- 
