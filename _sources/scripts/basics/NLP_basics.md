
# NLP basics

- [Kaggle - Basics of NLP for absolute Beginners](https://www.kaggle.com/discussions/general/231146#1265682)
- [WikiDocs - 딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/21698)

## Introduction

예상에 따르면, 접근 가능한 데이터 중에 오직 21%의 데이터 만이 structured 형태로 존재한다. 데이터는 우리가 말하면서, 트윗하면서, Whatsapp으로 메세지를 보내는 등의 다양한 형태의 활동을 하면서 생성된다. 그 중에 대부분의 데이터가 textual form으로 존재하고, 이는 굉장히 unstructured한 형태이다.

## 1. corpus, tokens, engrams

![../images/5e880971363eccfc191c6dd51264f581_MD5.png]

Corpus는 `a collection of text documents` 로 정의된다. 예를 들어 news들로 구성된 dataset은 코퍼스라고 할 수 있고, tweet들로 구성된 twitter dataset도 하나의 코퍼스라고 말할 수 있다. 이러한 하나의 코퍼스는 여러 documents로 이루어지고, document는 paragraph(구, 절)로 이루어지고, paragraph는 sentence(문장)으로 이루어지고, 하나의 문장은 token()으로 이루어진다.

그러면 token이란 무엇인가? token은 word, phrase, engram이 될 수 있다. engram은 `group of n words togather`로 정의되는 단어 뭉치다.

예를 들어

> I love my phone

이 문장을 볼 때 uni-gram(n=1)로 보면 I, love, my, phone 의 형태로 token이 4개다. Di-gram(n=2)로 보면, I love, love my, my phone으로 3개의 토큰으로 분간된다.

토큰의 문장(sentence)일 수도 있다. 이럴 경우에 마침표가 대부분은 문장의 구분자로 사용될 수 있지만, 문제는 가끔 안그럴 경우가 있다는 것이다. 적절하게 해당 언어에 적합한 tokenizer를 사용해야한다. 한국어 - kss(korean sentence splitter)

## 2. tokenization

token에 대해서 알았으니 문장과 구를 우리가 정의한 토큰(words, numbers, engrams or symbols)으로 만드는 것이 tokenization일 것이다. a process of splitting a text object into smaller units which are also called tokens.

### 2.1. White-space tokenization

가장 많이 쓰이는 tokenization 방식이 white-space tokenization방식이다. 그냥 단순하게 띄어쓰기를 기반으로 token을 분간하는 것이다.

### 2.2. Regular expression tokenization

정규표현 토큰화. splitting pattern을 정규식으로 분간할 수 있다. 정규 표현식은 문자열의 패턴을 정의하고 일치하는 부분을 찾는데 사용된다.

```python
S = 'Football, Cricket; Golf Tennis'
re.split('r[;,\s]', S)
Tokens = "Football","Cricket","Golf","Tennis"
```

> re.split('r[;,\s]', S)
> >; , \s(공백) 문자열 중에 해당 3개와 같은 것으로 분할해라.

### 토큰화 고려사항

1. 구두점이나 특수 문자를 단순 제외 NO
   - 날짜 사이의 /, 구두점 in Ph.D, 소수점
2. 줄임말과 단어 내에 띄어쓰기가 있는 경우
   - rock 'n' roll은 하나의 단어이지만 중간에 띄어쓰기가 존재함. 띄어쓰기가 있어도 하나의 token으로 보아야함.
   - (') apostrophe

### 2.3 한국어에서 토큰화의 어려움

1. 교착어의 특성
   - `조사(preposition)`라는 것이 존재. 띄어쓰기 없이 바로 뒤에 붙음. 띄어쓰기 단위로는 처리가 불가.
   - 따라서 형태소 단위로 단어를 구분해주어야함.
2. 띄어쓰기가 잘 안 지켜진다.
   - 띄어쓰기를 안해도 의미적으로 이해는 간다.
   - 1933년에 띄어쓰기가 보편화 되었으니 100년도 안되었다.
   - '모아쓰기'라는 한국어적인 특징이 존재한다.
   - corpus 에서 전반적으로 영어에 비해 띄어쓰기가 잘 안지켜졌을 확률이 높다.
3. 한국어는 어순이 중요치 않다.
   - 이건 토큰화보다는 모델링에서의 문제인데, 이전 단어가 주어질때 다음 단어가 나타날 확률을 구할때 어순이 중요치 않다는 것은 어떤 단어는 출현이 가능하다는 뜻이 된다.
   - 확률에 기반한 언어 모델()이 성능이 제대로 안나올 가능성 크다.

## 3. Normalization 정규화

![../images/9b29442026783ce1e7672cbd8ce504d9_MD5.png]

우리가 익히 알고 있는 정규화는 curr - min / max - min이다. 언어학과 자연어 처리에서 `morpheme(형태소 : 의미를 가진 가장 작은 단위)`라는 것이 단어의 기반으로 정의된다. 보통 token이라는 것은 두 개 이상의 morpheme의 합으로 구성된다. 접두사(prefix) 접미사(suffix)가 단어의 형태에 따라 변형되어 붙는다.

정규화는 'converting a token into its base form'하는 과정이다. inflection form → base form.

1. reducing the # of unique tokens present in the text
2. removing the variations of a word in the text
3. removing redundant information

### 3.1 stemming 어간 추출

laughing, laughed, laughs, laugh → laugh
단점 : 가끔 사전에 없는 단어를 만들 수도 있다. 그래서 좋은 normalization은 아닐 수 있다. 또한 winning 같은 경우 원래의 stem은 win인데 winn으로 만들 수 있다.

```python
from nltk.stem import WordNetLemmatizer
from nltk.stem import PosterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
```

보통 어간 추출 속도가 표제어 추출보다 빠르다.

### 3.2 lemmatization 표제어 추출

Lemma 표제어는 '기본 사전형 단어' 정도의 의미를 가지고 있다. 표제어 추출을 위해서는 기본적으로 POS(part of speech)가 필요하다. 형태학적 파싱(morphological parsing)을 하게되면 어간(stem)과 접사(affix)로 단어를 쪼개게 된다. 이러한 과정을 통해서 더 이상 쪼갤 수 없는 단위로 의미를 쪼개는 것이다. 이런 과정을 위해서 품사 정보를 고려하여 단어의 원형을 추출하는 것이 의미적으로 정확하고 일관된 결과를 얻는데 도움이 된다.

### 3.3 POS(part of speech tags)

[KoNLPy 한국어 처리 패키지](https://datascienceschool.net/03%20machine%20learning/03.01.02%20KoNLPy%20%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%B2%98%EB%A6%AC%20%ED%8C%A8%ED%82%A4%EC%A7%80.html)

품사란 문장내 단어의 문맥, 기능 그리고 활용을 정의하는 것이다. 품사는 문장 내의 다른 단어들 과의 관계로 정의된다. 머신러닝 모델이나 rule-based 모델들은 단어의 품사를 알아야 적용이 가능하다.

## 4. 문법 Grammer

### 4.1 Constituency Grammar

### 4.2 Dependency Grammar

words of a sentence are dependent upon other words of the sentence

## 5. Subword Tokenizer 알고리즘

> Birthplace = Birth + Place

아무리 많이 학습시켜도 모르는 단어가 학습과정에서 나오기 마련이다. 이를 OOV(out-of-vocabulary), UNK(unknown token)이라고 말한다. OOV문제를 일으키는 단어는 보통 더 작은 단위로 쪼개면 아는 2개로 해석될 수 있는 합성어, 희귀 단어 혹은 신조어 인 경우가 많기 때문에 단어를 더 쪼개갰다는 의미이다.

### 5.1 Byte-Pair Encoding(BPE) 1994

[huggingface_DOC](https://huggingface.co/learn/nlp-course/chapter6/5?fw=pt)

> aaabdaaabac → (aa → Z) ZabdZabac → (ab → Y) ZYdZYac → (ZY → X) XdXac

데이터 압축 알고리즘이다. 기본적으로 연속적으로 가장 많이 등장한 글자의 쌍을 찾아서 하나의 글자로 병합하는 방식.

자연어 처리에서 BPE는 곧 subword segmentation 알고리즘을 말한다. 글자 단위에서 점차적으로 단어 집합을 만들어내는 bottom up 방식의 접근을 한다. 우선 훈련 데이터에 있는 단어들을 모든 글자 또는 유니코드 단위로 단어 집합을 만들고, 가장 많이 등장하는 유니그램을 하나의 유니그램으로 통합한다. 정리하자면 가장 빈번하게 등장하는 문자 혹은 subword의 쌍을 재귀적으로 합치며, 텍스트를 분할하는 방식이라고 볼 수 있다. 문제는 letter 수준에서 작동하기 때문에 단어 내의 내부 구조나 의미를 고려하진 않는다.

### 5.2 wordpiece tokenizer → for BERT

bpe가 빈도수에 기반하여 가장 많이 등장한 쌍을 병합하는 것 과는 달리, 병합되었을 때 코퍼스의 우도 likelihood를 가장 높이는 쌍으로 구성. 모든 단어 앞에 _를 붙이고 기존에 없던 띄어쓰기 추가. 되돌릴때는 띄어쓰기 모두 없애고_ 를 띄어쓰기화 하면 된다.
BPE랑 비슷하긴 한데, 단어 수준에서 작동한다는게 다르다. BPE가 letter → token(subword) bottom up 방식이었다면, wordpiece는 word → token(subword) topdown 방식이라고 볼 수 있다. 또한 차이점은 단어 경계를 표시하는 특수 토큰[CLS],[SEP]등을 사용하여 서브워드를 생성할 수 있다는 것이다.

### 5.3 SentencePiece

사전 토큰화 작업(pretokenization) 없이 전처리를 하지 않은 데이터(raw data)에 바로 단어 분리 토크나이저를 사용할 수 있음. 단어 분리 토큰화 수행 → 어떤 언어에도 바로 적용 가능.

### 6. Libraries

1. spacy

- c 기반, 빠름
- 그냥 이거 써라

2. nltk

- 쓸데없이 선택지 많음
