---
layout: post
title: NLP 1차 수업 정리
category: 
    - mldl
    - nlp
description: >
  자연어 처리에 대해서 제대로 배워보고 정리해보자. \
  [유튜브 김기영님의 자연어처리 4개 강의](https://youtube.com/playlist?list=PLrLEKGJAgXxL-R9IqDH7HANWXRsS900tF)에 대해서 하나씩 정리해보는 시간을 가져보려 한다.
image: /assets/img/blog/nlp/wall.jpeg
accent_image:
  background: url('/assets/img/blog/nlp/wall.jpeg') center/cover
  overlay: false
accent_color: '#ccc'
theme_color: '#ccc'
invert_sidebar: false
sitemap :
  changefreq : daily
  priority : 1.0
---
* toc
{:toc}

## Introduction to NLP

![nlp tasks](/assets/img/blog/nlp/nlp.png)
다양한 NLP tasks
{:.figcaption}

* NLP는 2018년 BERT가 나오면서 10% 이상의 성능향상을 이루었고, 지금은 그 이후 또 10% 이상의 성능향상을 이루었다.
* 연구성과는 **open source**화가 잘 되어있다. 하지만 누구나 노력해서 읽고 사용하는 것은 아니다.
* task에서는 좋은 모델이라해도, 서비스에서는 그렇게 좋은 서비스로 사용되기는 힘들다. 100번에 1번 틀리는 서비스는 좋은 서비스가 아니다.
* AI는 새로운 자동화 기술이다. 빅데이터와 머신러닝은 자동화가 불가능할 것 같은 영역에 대한 새로운 자동화 접근법이다.
* 머신 > 러닝 > 빅데이터(복잡성) 순서로 배워나갈 것이다.

**GLUE**\
The General Understanding Evaluation benchmark\
[GLUE](https://gluebenchmark.com/leaderboard)
사람이 하는 것 보다 더 잘하는 분야도 있다? -> 정리필요

## Tokenizer - 단어 나누기, vocab len

1. 띄어쓰기 단위
   * (pro)명료하고 적용되기 쉽다.
   * (con)하나의 형태소(맛있+)에서 파생어(맛있다.맛있었다...)들도 전투 다르게 인식되기 때문에 단어사전이 매우 커진다. **비효율적**
2. 문자 단위
   * (con)각 token이 의미를 담지 못한다. 학교가 학,교로 2개의 토큰으로 되기 때문에. 이는 중국어와 같은 언어에서는 의미가 있을수도 있겠다.
3. **subword 단위**
   1. 형태소 단위
      * (pro) 매우 효율적
      * (con) 언어 지식이 필요함, 컴퓨터가 알아서 할 수 없음 -> 요즘은 덜 씀
   2. BPE(byte-pair encoding)
      * 전체 문서를 문자 단위로 쪼갠 뒤, 빈번하게 나오는 문자들을 묶어서 단어사전의 수를 줄임.
      * Bottom pu 접근방식
      * 학,교 < 학교
      * 30000개 정도가 될 때까지 이 과정을 반복, 그래서 거의 대부분 tokenizer들이 보면 30000개 정도인 경우가 왠지 많더라.

## NLP - Embedding

자연어(프로그래밍 언어가 아닌 인간이 쓰는 언어)를 다루는 문서요약, 감성분석, 질의응답, 문장생성을 아우른다. 그런데 **컴퓨터가 어떻게 인간의 언어를 알아듣는가?** 컴퓨터는 언어를 그대로 이해하는 것이 아니라 **숫자**로 만들어서 이해하게 해야한다.

* 이를 embedding(일상언어->숫자)이라고 한다.
* 서로 다른 모델은 서로 다른 임베딩 방법을 가지고 있다.
* 언어를 무작위하게 숫자를 붙이는 방법 -> 유사한 단어, 유사한 문장은 유사한 숫자가 부여 되도록 표현하는 방향으로 발전하게 된다(attention이 생각나는 부분이다.)

* subword tokenizer도 학습 필요하다. 학습한 텍스트 데이터셋에 따라 결과가 다르다.
  * tokenizer 학습은 model 학습과 별도, 선행 된다.
* 모든 언어처리 과정은 tokenizer로 부터 시작한다.
* 필요한 task과 관련된 domain에 학습된 것을 골라야 결과가 좋을 수 밖에 없다.
  * tokenizer -> embedding -> model 순으로 학습에 영향을 미치니깐 당연하다.
* vocab.txt라고 되어있는 단어사전이 github model repo안에 포함되어있다.

### Embedding 1 - Bag of words(Term frequency)

|  | 학교에 | 가서 | 수업을 | 들었다 | 온건 | 오랜만이다 | 친구 | 얘기를 |
|---|---|---|---|---|---|---|---|---|
| 학교에 가서 수업을 들었다. 학교에 온건 오랜만이다. | 2 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 학교에 가서 친구 얘기를 들었다. | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 |
| 내일 가서 뭐 먹지? | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

[(참고) 마크다운 테이블 쉽게 만드는 사이트](https://www.tablesgenerator.com/markdown_tables)

* 단어를 빈도(frequency)로 나타내자!
  * 쉽고 직관적이지만 직관적으로 문장을 숫자로 변환할 수 있다.
  * 단어 빈도를 기반으로 문서 유사도를 쉽게 파악할 수 있다. 문장 속에 비슷한 단어가 많이 들어있으면 서로 비슷한 의미의 문장이 아닐까라는 접근법.
* 빈도는 **순서**에 대한 고려가 없다.
  * '좋다가 말았다' 처럼 좋다의 의미가 아닌데 좋다로 판단해 버릴수도 있다.
  * 세상 모든 단어에 숫자를 붙여야 한다. TOO MANY!
  * 재구성이 불가능하다.

### Embedding 2 - TFIDF(Term frequency with weight)

TFIDF(단어빈도-역문서빈도,Term Frequency-Inverse Document Frequency)
{:.note title="Definition of TFIDF"}

* (빈번하게 나타나지만, 문장의 특징을 나타내진 않는 a,the,조사)조사와 같은 것의 가중치를 낮출 순 없나?
* 단어가 나온 문장의 수로 나눠주자!
* 다른 문장에는 자주 안나오지만 특정 문장에서 빈번하게 등장하는 단어 -> **KEYWORD**를 뽑아보자!
* $$TFIDF = log(wordFreq/(sentenceFreq + 1))$$ /0을 피하기 위해서 뒤에 처리
* [sklearn.feature_extraction.text.TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

>하지만 여전히 단점이 많다. **순서와 맥락**을 고려하지 못한다. 언어에서 의미는 순서에 따라 전혀 달라지기도 하기 때문에 이를 보완하는 embedding이 필요했다.
{:.note title='BOW,TFIDF 한계'}

### Embedding 3(2013) - Word2Vec

> King - man + woman = queen \
> [1.5,0,0] - [0,1,0] + [1.5,1,0] = [3,0,0]
{:.lead}

**방식**

1. 초기 단어를 임의의 배열로 세팅
2. 주변 단어의 배열로 관심단어 배열을 만들기
3. 이 과정을 내가 가진 모든 텍스트에 대해 반복하여 학습

**장점**

1. 주변단어가 비슷한 단어들은 배열 구조가 유사해 질 것이다. -> 유사단어끼리 유사한 배열을 보여줄 것을 기대한다.
2. 매우 빠르고 합리적인 성능으로 상용시스템에서도 현재 많이 쓰인다.
3. 평균을 내기 때문에 bow에 비해서 0값이 잘 안나온다. bows는 sparse representation이기 때문에 필요없는 단어에 대한 표현은 전부 0처리하는 one-hot encoding방식이기 때문에 데이터 효율이 떨어진다.
4. 소수를 통해서 엄청나게 유연한 표현이 가능하다.([dense representation](https://wikidocs.net/33520))

**NPLM(Neural Probabilistic Language Model) vs Word2vec**

| |word2vec|NPLM|
|---|---|---|
|model|Autoencoding model|Autoregressive model|
|방향|bidirectional|oneWay|
|문장이해도|좋음|떨어짐|
|genrative|X|O|