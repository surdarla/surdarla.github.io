# LangChain

```{figure} https://cdn.analyticsvidhya.com/wp-content/uploads/2023/06/Screenshot-2023-06-09-at-4.48.41-PM.png

the langchain logo
```

[documentation](https://python.langchain.com/docs/modules/chains/document/)

> LangChain은 LLM을 포함하는 앱을 **만들기 위한** framework이다.

LangChain의 핵심 아이디어는 다양한 구성 요소들을 말 그대로 연결하여 (LLM 자체를 개발하는 것보다는) 살짝  high level에서 개발할 수 있도록 하는 것이다. 이를 위해서는 구성 요소들에 대해서 알아야 할 것이고, 그 다음에는 어떻게 연결하는지를 알아야 할 것이다. 이 프레임워크의 목적은 `LLM을 이용한 App`개발이다. LLM 개발이 아니라는 것에 방점을 찍어야할 것이다.

LangChain은 API에 기반하여 LLM에 연결하는 기능이 기본적으로 준비되어있다. 이를 이용해서 OpenAI gpt4와 같은 모델을 불러와서 사용할 수 있다. 또한 이뿐만이 아니라 (react처럼) 다양한 컴포넌트들이 준비되어있다. 이것들이 LangChain의 추상화된 구성요소들을 이룬다.



1. Schema
   1. llm과 상호작용하는 가장 기본적인 인터페이스다
   2. `system`,`ai`,`human` 3 종류의 사용자를 지원한다
      1. `system` : ai에게 해야할 일을 알려주는 context
      2. `ai` : ai가 응답한 내용을 보여주는 상세 메시지
      3. `human` : 사용자가 원하는 내용, input
2. Models
   1. langchain은 인터페이스만을 지원하며, llm은 api로 연결하거나 개인적인 것을 사용해야한다.
3. Prompts
   1. text를 때려넣는 방법이 있고
   2. 이미지, 오디오 등의 고차언의 데이터 유형도 요즘은 넣을 수 있다.
   3. `prompt template`를 사용해서 `args`처럼 넣어주는 방식으로도 가능하다.
   4. `output parser`: 구조화된 정보를 output으로 받고싶을때 llm의 응답을 구조화함.
4. Indexes
5. Memory
6. Chains
7. Agents

### Schema

데이터 구조를 말한다. 여기서 document를 읽다보면 `runnable`이라는게 참 많이 나오던데 이에 대해서 나중에 정리할 필요가 있을수도 있겠다. 암튼 `chain.input_schema.schema()`라고 하면 JSON 형식으로 input이 뭐가들어갔는지 정리되어서 나온다. output schema도 마찬가지라고 볼 수 있다. `pydantic` 이란 것도 나오는데 파이썬 라이브러리로 뎅터 파싱과 검증을 간편하고 빠르게 해주는 도구라고 한다. 복잡한 데이터 유형을 모델링하고, 이를 파이썬 Typing과 함께 사요애서 유효성(validality)를 검사할 수 있다. Typing(타입 힌트)를 기반으로 작동하는데 이를 좀 더 복잡한 데이터 유형으로 확장하는 라이브러리라고 보인다. (FastAPI와 사용하면 좋다고 한다.)

```{figure}https://velog.velcdn.com/images/jjlee6496/post/f5c069d7-04f0-4a33-a117-ba6709d7fe64/image.png
```


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
