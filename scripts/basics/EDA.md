# EDA(Exploratory Data Analysis) 탐색적 분석

데이터를 정제하고 변수를 처리했으면 인쟈 데이터 탐색을 할 차례다. 데이터를 제대로 분석하기 전에 그래프나 통계적인 방법으로 자료를 직관적으로 바라보는 과정이라고 할 수 있다.

## 의의

1. 데이터가 표현하는 현상 이해
2. 데이터의 잠재적인 문제 발견
3. 데이터 수집할지 말지를 결정하게 됨
4. 문제 정의 단계에서 미쳐 발생하지 못했을 다양한 패턴 발견
5. 기존의 가설을 수정, 새로운 가설을 세우게 됨

## 필요 지식

1. 개별 데이터를 관찰함에 있어서, 앞뒤의 데이터 만을 보고서는 이상패턴에 대한 관찰을 할 수 없음 $\to$ `sampling 기법`을 통해서 표본 추출.
2. 시각화 이후에 이에 대한 의미를 통계적으로 찾기 위해 `확률분포`에 대한 이해 필요

## 기초 통계 지식

### 대표값 Representative Value

주어진 자료를 특정 값으로 대표하기.
컬럼들간의 비교를 할 시에 사용될 수 있다.

1. 평균 mean
   - 산술평균 numerical mean
     - $(x_1 + x_2 + ... + x_n) / n$
     - $\sum_{i=1}^n x_n \div n $
     - np.mean(x)
   - 기하평균 geometric mean
      - $\sqrt[n]{\sum x_n}$
      - np.exp(np.mean(np.log(x)))
      - np.prod(data) ** (1 / len(data))
   - 조화평균 harmonic mean
     - something
   - 가중평균
      - 각 자료값이 가지는 중요성이 다른 경우
      - 상대적 중요도 (w)

2. 중위값 median

- numpy.median(a(array_like), axis=None, ...) $\to$ array_like
- torch.median(input, dim=-1,keepdim=False,*,out=None) $\to$ Tensor
- torch.quantile(input,q=0.5,dim=None,keepdim=False,*,interpolation='linear',out=None) $\to$ Tensor

3. 최빈값 mode

```{admonition} 극단값이 1개 있을떄
:class: dropdown

이런 경우 산술평균으로 하면 해당 outlier로부터 매우 큰 영향을 받을 수 밖에 없다. 그런 경우에는 mean보단 median,mode가 더 representative value로 적합해질 수 있다.
```

### 분포 Distribution

대표값 만으로는 데이터가 어떤 모양을 이루는지 알 수 없다. 대표값은 점 이기 때문에. 이를 위해서 분위수 max min 분산 편차 등의 방식으로 `흩어진 정도`를 파악한다.

#### 1. 분위수 fractile

n개의 데이터를 작은 수에서 부터 큰 수의 순으로 놓고 몇 등분을 하기. 경계 부분의 수치를 분위수라고 한다.

- 1 $\to$ 4로 갈수록 커지게됨
- 사분위수의 범위 IQR(Interquartile Range) : $IQR = Q_3 - Q_1 = 50\%$
- q2 = median
- count는 분위수 모두 같다.
![4분위수](/images/4fractile.png)

#### 2. 편차 deviation $\sigma$

데이터 값과 평균값의 차이\
편차는 개별 데이터에 대하여 계산된다.
$$\sigma_i = x_i - \mu$$

#### 3. 분산 variance

편차를 하나의 지표로 데이터의 특성(얼마나 흩어져 있는가)에 대한 표현

$$\tag{variance}
\sigma^2 : \text{모분산}\\
s^2 : \text{표본분산}\\

\begin{equation}
\begin{split}
Var(X) =& \frac{1}{n}\sum_{i=1}^n(x_i-\mu)^2\\
=& \frac{\sum (Y_i - \bar{\mu}^2)}{N}\\
=& E\Big[ (X-\mu)^2\Big]\\
=& E[X^2] - E[X]^2
\end{split}
\end{equation}
$$

#### 4. 이상치 outlier

평균에서 멀리 떨어져 있는 값으로 대표값을 설정할때 영향을 준다. 평균에 큰 영향을 주는 요소이다.

#### 5. 변동계수 Coefficient of Variation

두 개의 데이터가 흩어진 정도를 비교하는 경우\
측정 단위가 다른 자료를 비교할 때 사용\
표준편차를 표본평균이나 모평균 등 산술평균으로 나눈 것\

$$
CV = \frac{s}{\mu}
$$

### 확률과 확률 분포 Probability Distribution

#### 1. 확률 Probability $P(A)$

결과는 우연히 정해지지만 결과를 예측 또는 기대를 할 수는 있다. 동일한 조건에서 동일한 실험을 무수히 반복하여 실시할 때, 어떤 특정한 사건이 발생하는 비율을 `확률` 이라고 말한다.

$$
P(A) = \frac{\text{A 사건이 일어나는 경우의 수}}{\text{모든 사건이 일어나는 경우의 수}}
$$

#### 2. 확률 변수 Random Variable

- 실험 : 동전을 무작위로 던져서 앞 뒤 확인
- 확률 : 앞 1/2 뒤 1/2
- 결과 tagging : 앞 1 뒤 0

여기서 결과 tagging, 실수값을 부여하는 것을 변수라고 한다. 사건 X(실험의 결과, 앞or뒤)에 수치를 부여해서 수학적인 개념으로 넘긴 것이다.

이산확률변수(discrete random variable)는 int label처럼 값이 분리된 것이고, 연속확률변수(continuous random variable)는 금액, 물의 양 과 같이 연속적인 것이다.

```{admonition} 연속이냐 이산이냐
:class: dropdown

그렇다면 시간은 이산확률변수일까 아니면 연속활률변수일까? 1초 2초 처럼 셀 수 있는 것으로 붸긴하지만 실제로는 딱 떨어지지 않는다.

특히 가장 큰 이산확률변수와 연속확률변수의 차이는 확률을 P(X=x)로 표기할 수 있는가 없는가 이다. 물을 변수라고 한다면 정확한 100ml를 따르는 확률 P(X=100ml)는 사실상 0에 가깝기 때문에 이는 연속확률변수라고 보기 힘들게 되는것이다.
```

```{admonition} 정규분포 normal distribution
:class: tip

많이 들어봤을 정규분포는 대표적인 연속확률변수의 확률 분포다.
```

위에서 이산확률변수와 연속확률변수의 차이 때문에 연속확률변수는 확률분포함수 f(x)를 도입하며, f(x)를 a에서 b까지 적분함으로써 확률변수의 값이 a와 b사이에 있을 확률을 구한다.

#### 3. 확률 분포 Probability Distribution

event 시행에서 확률변수 random variable이 어떤 값을 가질지에 대한 확률을 나타낸다. 확률변수가 취하는 값들의 집합이 자연수의 부분집합과 일대일 대응한다면 이산확률분포, 실수의 구간을 이루면 연속확률분포

##### 3-1. 이항분포 Binomial Distribution

n번의 독립 베르누이 시행(1 event $\to$ o or x)에서 성공확률이 p일 때의 확률 분포. 만약 충분하게 n의 수가 많아지면, 분포는 좌우대칭의 정규분포에 가까워진다.

```{margin}
n : 시행event의 횟수
X=k : n회의 실행에서 k번이 뒷면이 출현
P(X=k) : 위의 확률
```

$$
B(X;n,p) = {}_n C_x p^x(1-p)^{n-x} = {}_n C_x * p^k * q^{n-k} \\
{}_n C_x = \frac{n!}{x!(n-x)!}\\
$$

##### 3-2. 균일분포 Uniform Distribution

각 사건이 일어나는 확률이 같은 분포.

$$
이산확률분포+균일분포= \begin{cases}
x={1,2,3,...,n}\\
P(x=k) = \frac{1}{n}\\
\mu = \frac{n+1}{2}\\
\sigma^2 = \frac{n^2-1}{12}
\end{cases}
$$

##### 3-3. 정규분포

가우시안 분포라고도 불리는 연속확률분포 중에 가장 유명한 분포이다. $\mu$ 평균값을 중심으로 대칭을 이루는 종 모양이다. 이항분포의 n 시행 횟수를 늘리면 그 분포는 정규분포와 가까워진다. {prf:ref}`Central-limit-theorem(CLT)<my-theorem>`(중심극한정리)에 의하면 독립적인 확률변수들의 평균은 정규분포에 가까워지는 성질이 있다.

```{prf:theorem} Central-limit-theorem(CLT)
:label: my-theorem

Central limit theorem(CLT)

**전제** Given $X_1, X_2, X_3,...X_n$ with 독립항등분포, each $E(X_i) = \mu$ and $\sigma$, $\xi_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sqrt n \sigma}$라고 둘 때,

**결론** $\xi_n$은 표준정규분포로 분포수렴한다.


**DEF** 무작위로 추출된 표본의 크기가 커질수록 표본 평균의 분포는 모집단의 분포 모양과는 관계없이 정규분포에 가까워진다.
```
