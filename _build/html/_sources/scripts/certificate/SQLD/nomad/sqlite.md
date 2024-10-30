()=
# SQLite

## SQLite란?

SQLite는 서버가 필요 없는 데이터베이스이다. SQLite는 파일 기반의 데이터베이스로, 서버가 필요 없이 데이터베이스를 사용할 수 있다. SQLite는 C언어로 작성되어 있으며, 매우 가볍고 빠르다. SQLite는 오픈 소스이며, 무료로 사용할 수 있다.

이러한 특성 때문에 SQLite는 모바일 기기나 임베디드 시스템에서 많이 사용된다. SQLite는 안드로이드, iOS, Windows Phone 등의 모바일 운영체제에서 기본 데이터베이스로 사용된다. 또한 소규모 프로젝트에서도 많이 사용한다. 하지만 프로젝트 규모가 커지고 다수의 사용자가 사용하는 경우에는 SQLite보다는 MySQL, PostgreSQL, Oracle 등의 데이터베이스를 사용하는 것이 좋다.

## 1. Install sqlite3

본인의 컴퓨터에 sqlite3를 설치하는 방법은 크게 두 가지가 있다.

1. sqlite3 page에 방문해서 직접 apk 다운로드
2. scoop, brew를 통해서 패키지를 한번에 다운

scoop은 이번에 처음 사용해봤다. brew는 mac을 사용할 때, 워낙 유명했기에 많이 사용했었는데, 윈도우에도 비슷한 패키지 매니저가 있는 것은 처음 알았다. 이제 powershell에 절대로 익숙해 질 것 같지 않는 명령어는 사용하지 말고, 이제 scoop을 사용하자. 우선 [scoop을 깔고](https://scoop.sh/#:~:text=Set%2DExecutionPolicy%20%2DExecutionPolicy%20RemoteSigned%20%2DScope%20CurrentUser%0AInvoke%2DRestMethod%20%2DUri%20https%3A//get.scoop.sh%20%7C%20Invoke%2DExpression), 그 다음에 [scoop sqlite3](https://scoop.sh/#/apps?q=sqlite) 여기에서 맨 위에 있는 sqlite3에 명령어 두 개를 터미널에 입력해주면 된다.

그리고 노마드쌤이 강추하는 beekeeper studio community를 설치했다. [여기](https://www.beekeeperstudio.io/get-community)에서 다운로드 받을 수 있다. 이메일만 써주면 어려울 것이 없다. 예전에 tibero database를 사용하기 위해서 dbeaver를 사용했던 경험이 있는데, 이것과는 어떤 차이가 있는지 궁금했다. 찾아보니 dbeaver는 좀 고급 사용자를 위한 것이고, beekeeper studio는 상대적으로 신생 오픈소스로 더 쉽게 사용할 수 있다고 한다. 그래서 나는 beekeeper studio를 사용하기로 했다.

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
