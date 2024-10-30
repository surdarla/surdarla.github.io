()=
# SQL intro

## 1. 왜 sql을 배워야 하는가?

데이터 자체가 가치다. 데이터는 너를 규정함과 동시에 너의 다음 스텝을 예측하며 강요할 수도있다. 이러한 데이터가 저장되는 곳이 database이고, 데이터베이스와 통신하는 것이 SQL이다.

## 2. orm vs sql

ORM : object relational mapping

orm은 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것이다. 즉, 객체를 통해 데이터베이스를 조작할 수 있게 해준다. orm은 sql을 사용하지 않아도 된다. 하지만 orm을 사용하면 sql을 사용하지 않아도 된다는 것은 orm을 사용하지 않는 것보다 *더 많은 sql을 알아야 한다는 것*이다.

## 3. SQL, RDBMS

- 1970년대에 만들어졌다.
- Structured Query Language라는 것의 줄임말이다.
- RDBMS : relational database management system 관계형 데이터베이스와 통신하게 해준다.
- 데이터베이스는 데이터를 저장하는 곳이다. 데이터베이스는 테이블로 구성되어 있다. 테이블은 행과 열로 구성되어 있다. 행은 레코드, 열은 필드라고 부른다. 관계형은 이렇게 엑셀처럼 하는 것을 말한다.
- Declarative 선언형 언어이다. 즉, 명령형 언어에서처럼 문제 해결을 위해서 구체적인 절차와 로직을 작성할 필요가 없다. 그냥 원하는 것만 띡 써버리면 된다.
- 이식성이 있다? Portable
  - sqlite code $\to$ mysql code $\to$ oracle code $\to$ sql server code  ??
  - 데이터베이스 별로 규칙이 있다.
- Standardized 표준이 있다.
  - 그런데 다 이식된 것은 아니다.

## 4. Many Languagues of SQL

1. DDL : Data Definition Language
   - 데이터베이스의 구조를 정의하는 언어
   - CREATE, ALTER, DROP
2. DML : Data Manipulation Language
   - 데이터를 조작하는 언어
   - SELECT, INSERT, UPDATE, DELETE
3. DCL : Data Control Language
   - 데이터를 제어하는 언어
   - GRANT, REVOKE
4. TCL : Transaction Control Language

```{tableofcontents}
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
