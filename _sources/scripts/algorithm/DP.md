(dp)=
# Dynamic Programming

Knapsack problem 이라는 배낭 채우기 문제는 워낙 유명하고 DP를 처음 접할 때 대부분 이것으로 접하게 된다.

```{admonition} knapsack problem
배낭의 최대 용량은 W이며, 이를 초과해서 보석을 담으면 배낭이 찢어진다. 각 보석들의 무게와 가격은 알고 있다. 배낭이 찢어지지 않는 선에서 가격 합이 최대가 되도록 보석을 담는 방법을 return 해라.
```

여기에는 두 가지 종류의 문제가 있다. 보석을 자를 수 있는 `fractional knapsack problem`과 자를 수 없다고 가정하는(덩어리로) `0-1 knapsack problem`이 있다. 동적계획법은 후자의 문제를 다룰 때 사용된다.

DP는 큰 문제를 작은 문제로 쪼개서(Devide-and-Conquer), 이전 계산 결과를 저장해서 반복을 줄이는(Memorization) 이 두 가지를 활용해서 문제를 해결한다. 워낙 유명한 피보나치 수열문제는 재귀함수를 이용하는 dp를 사용해서 풀 수 있다.

```python
memo = {1:1,2:1}
def fibo(n):
    # initialize
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # recursive memo
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
```

그냥 memo를 안해도 풀 수 있긴 하지만, 이렇게 재귀적으로 앞의 계산 결과를 뒤에서 활용하는 문제는 저장을 하냐 안하느냐에 따라서 n이 커질 경우에 압도적으로 시간복잡도가 줄어든다. 이러한 DP를 `0-1 knapsack problem`에 적용하려면 `최적의 원리(principle of optimality)`가 성립하는지 확인해야한다. 최적의 원리란

```{admonition} Principle of Optimality
어떤 문제의 입력 사례의 최적해가 그 입력 사례를 분할한 부분 사례에 대한 최적해를 항상 포함하고 있으면, 그 문제에 대하여 최적의 원리가 성립한다.
```

**최적 부분집합 성립 알아보기**

- $A$ : $n$개의 보석들 중 최적으로 고른 부분집합
- $A$가 $n$번째 보석을 포함하고 있지 않다면, $A$는 $n$번째 보석을 뺀 나머지 $n-1$개의 보석들 중에서 최적으로 고른 부분집합과 같아. $\to$ 최적의 원리 적용가능
- $A$가 $n$번째 보석을 포함하고 있다면, $A$에 속한 보석들의 총 가격은 $n-1$ 개의 보석들 중에서 최적으로 고른 가격의 합에다가 보석 $n$의 가격을 더한 것과 같다.
- $P[i,w]$란 i개의 보석이 있고 배낭의 무게 한도가 w일때 최적의 이익

$$
P[i,w] = \begin{cases}
P[i-1,w] &\text{if } w_i > w\\
\max\{v_i+P[i-1,w-w_k],P[i-1,w]\} &\text{else}
\end{cases}
$$

i번째 보석이 배낭의 무게 한도보다 무거우면 넣을수 없음으로 i번째 보석을 뺀 i-1개의 보석들을 가지고 구한 전 단계의 최적값을 유지한다. 그렇지 않을 경우 i번째 보석ㅇ르 위해 i번째 보석만큼의 무게를 비웠을 때의 최적값에 i번째 보석의 가격을 더한 값 or i-1개의 보석들을 가지고 구한 전 단계의 최적값중 max를 취한다.

## [12865 : 평범한 배낭](https://www.acmicpc.net/problem/12865)

아주 클래식하고 그냥 맨 처음 만나는 배낭 문제다. 이름처럼 그래도 평범한 배낭 문제이다. 다른 배낭 문제 짱많으니깐 [백준 배낭문제 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=148) 여기 들어가서 구경해보자.

```python
import sys
input = sys.stdin.readline

def knapsack(n,k,items):
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1,n+1): # 물건 개수 늘리기
        w,v = map(int, items[i-1])
        for j in range(1,k+1): # 최대무게 늘리기
            if w <= j: # 물건무게가 여유용량보다 작으면
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else: # 이전 최적값 유지
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])
```

## referances

- [메시에 - dynamic programming:배낭채우기 문제(knapsack problem)](https://gsmesie692.tistory.com/113)

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