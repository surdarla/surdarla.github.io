# vscode snippet 만들기

```{article-info}
:avatar: /images/logos/my_favi.png
:avatar-alt: supposed to be surdarla logo
:avatar-link: https://surdarla.github.io
:avatar-outline: muted
:author: Surdarla
:date: Nov 21 Tue 13:21, 2023
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

```{figure} https://code.visualstudio.com/assets/docs/editor/userdefinedsnippets/ajax-snippet.gif
---
name : vscode snippet
align : center
alt : vscode code snippet gif
---
```

vscode를 사용하다보면 snippet이 기본적으로 제공되고 market에서도 install해서 사용할 수 있는 것에 익숙해지지만, 결국 나만의 생산성을 높이기 위해서는 본인만의 snippet을 만드는 것을 알아야한다.

기본적으로는 `built in snippet`이라는 내장 코드 조각이 존재한다. markdonwn이나 코딩을 하다보면 스리슬쩍 옆에서 추천해 주는 것이 이러한 것들이다. 이것들을 불러와 사용하려면 `ctrl,cmd + space`를 사용하면 된다.

## 나만의 snippet

사용자 코드 조각. 즉 나만의 snippet을 만드는 것에 대해서 알아보자. 사용자 코드조각은 `~.json` 파일로 생성되고 관리된다. 기본적으로 text 형태의 객체를 만들고 이를 불러오는 형식으로 json만한게 없기 때문인 것으로 보인다. 그리고 vscode는 기본적으로 `settings.json`으로 설정도 관리하는 것을 보면 json에 대해서 알아놓으면 나쁠 것이 없다.

`F1` $\rightarrow$ `Snippets:Configure User Snippets` $\rightarrow$ new global snippet로 들어가준다. 만약 markdown이나 특정 언어에 특화된 snippet이 필요하면 그걸 만들어 주면 된다.

```json
{
	// Place your global snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders.
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
}
```

이런 식으로 기본적인 snippet이 나온다. 읽어보면 규정해야할 것이 총 5가지 정도가 있다.

1. name : 해당 snippet의 이름, suggestion에 표시
2. scope : markdown, js, java 등 언어
3. prefix : `ctrl,cmd + space`를 사용시 어떤 단축어로 찾을지
4. body : 내용
5. description : 해당 snippet에 대한 설명

위와 같은 것들을 입력하면 된다. 다른 부분은 어려울 것이 없는데 body부분 입력에 있어서 몇 가지 알아야 할 것이 있다.

### body 입력 syntax

```json
	"basic snippet" : {
		"scope" : "\"${0:language}\"",
		"prefix" : ["snippet"],
		"body" : ["\"${1:title}\" : {",
					"\t\"prefix\" : [\"$2\"],",
					"\t\"body\" : [\"$3\"],",
					"\t\"description\" : \"$4\"",
					"}"
					],
		"description" : "basic snippet"
	},
```

json안에서 또 편하게 쓰기 위해서 해당 snippet안에서 사용할 snippet을 만들어 보았다. 이를 보면 알 수 있듯이 무조건 쌍따옴표를 사용해줘야한다. 그것을 위해서 전부 `"\` 이런식으로 사용한다. 그리고 줄바꿈을 하려면 `"",` 와 같은 식으로 해주고 tab이 필요할 경우에는 `\t`로 사용해준다.

그리고 placeholder가 존재하는데 `$~~` 이런식으로 표기된 것이다.

1. `$1`는 빈칸으로 보이지만
2. `${2:something}`으로 된 것은 something이 기본적으로 표기된다.
3. tab키를 사용해서 1,2,3... 순으로 이동하면서 수정이 가능하고
4. `$0`은 맨 마지막 순서를 규정한다. 0에서 한 번더 tab키를 누르면 해당 snippet 수정을 탈출한다.
5. ``

## reference

- [nJo2 - Visual Studio Code에서 코드조각(Snippets)을 슬기롭게 사용하는 방법](https://ux.stories.pe.kr/290)
- [Snippets in Visual Studio Code document](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets)

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