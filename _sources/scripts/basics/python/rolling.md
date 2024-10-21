()=
# rolling

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Oct 11 Fri 14:27, 2024
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

## window

시계열 분석에서는 window라는 것을 많이 사용하게 된다. window라는 것은 시계열 데이터를 일정한 크기로 나누어서 그 안에서 통계량을 계산하는 것을 의미한다. pandas에서는 이러한 window를 쉽게 구현할 수 있도록 rolling이라는 함수를 제공한다.

```{figure} ../../../images/sliding_window.png
---
name : sliding window
align : center
alt : sliding window
---
이렇게 일정한 크기의 window를 이동시키면서 통계량을 계산하는 것을 sliding window라고 한다.
```

## referances

- [[pandas] Windowing operations](https://pandas.pydata.org/docs/user_guide/window.html#window-generic)

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
