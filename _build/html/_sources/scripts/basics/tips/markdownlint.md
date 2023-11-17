# vscode markdownlint diableing MD~

obsidian이나 jupyter-book을 사용하다보면

    (something=)
    # 완전 이건 제목이야

이런식으로 사용해야할 경우가 있다. 그런데 MD036이라는 warning이 계속해서 `PROBLEMS`란에 뜨게된다. 이는 heading바로 위에 붙여서 text가 있을 경우에 markdown에서 경고를 하는 거라고 한다. linter를 사용하니깐 그 린터에 맞는 경고가 뜨는 것인데 이것이 계속해서 뜨는 것이다. 이러할 경우에 그냥 무시해도 되지만 쫌 거슬린다. 이를 위해서 `markdownlint.config`에서 설정을 좀 고쳐줘야한다.

## MD~~:false

[markdownlint_rules](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#rules)에 들어가보면 여러가지 markdown에서 지켜야할 룰들이 나온다. 대부분은 지키는 것이 좋지만, 개인의 블로그나 text editor의 환경에 따라서 노랑줄이 나올 수 밖에 없게 하는 경우가 있기 때문에 이에 대해서 비활성화 시키는 방법이 필요하다.

우선 `preference(cmd,ctrl + ,) > setting > extention > markdownlint`로 가서 `setting.json`을 열고 아래와 같이 입력해서 저장(cmd,ctrl + s)해주면 된다.

```json
"markdownlint.config":{
    "MD041":false,
    "MD036":false
},
```

나는 위와 같이 obsidian, jupyter-book을 위해서 document inner parsing을 위해서 두 개를 비활성화하고 있다.

## referance

- [vscode markdownlit - md009 해제하기](https://frhyme.github.io/vs-code/vscode_markdownlint_md009_disabled/)
