# pyeunjeon (python + eunjeon)

[![Build Status](https://travis-ci.org/koshort/pyeunjeon.svg?branch=master)](https://travis-ci.org/koshort/pyeunjeon)  

pyeunjeon은 [은전한닢 프로젝트](http://eunjeon.blogspot.kr/)와 mecab 기반의 한국어 형태소 분석기의 독립형 python 인터페이스입니다.  
pyeunjeon is a stand-alone python interface for morphological analyzer mecab and [project eunjeon](http://eunjeon.blogspot.kr/).

# Installation 설치

## Linux or Mac

```bash
# Install mecab first / mecab을 먼저 설치해주세요.
bash <(curl -s https://raw.githubusercontent.com/koshort/peunjeon/master/scripts/mecab.sh)

# Install eunjeon / eunjeon을 설치합니다.
pip install eunjeon
```

## Windows

```bash
pip install eunjeon
```

# Usage 사용법
```python
>>> from eunjeon import Mecab  # KoNLPy style mecab wrapper
>>> tagger = Mecab() 
>>> tagger.nouns("고양이가 냐 하고 울면 나는 녜 하고 울어야지")
['고양이', '나', '녜']
>>> # 빛 아래 유령
>>> poem = """
... 흘러내린 머리카락이 흐린 호박빛 아래 빛난다.
... 유영하며.
... 저건가보다.
... 세월의 힘을 이겨낸 마지막 하나 남은 가로등.
... 미래의 색, 역겨운 청록색으로 창백하게 바뀔 마지막 가로등
... 난 유영한다. 차분하게 과거에 살면서 현재의 공기를 마신다.
... 가로등이 깜빡인다.
...
... 나도 깜빡여준다.
... """
>>> tagger.morphs(poem)  # 형태소 단위로 나누기
['흘러내린', '머리카락', '이', '흐린', '호박', '빛', '아래', '빛난다', '.', '유영', '하', '며', '.', '저건가', '보', '다', '.', '세월', '의', '힘', '을', '이겨', '낸', '마지막', '하나', '남', '은', '가로등', '.', '미래', '의', '색', ',', ' 역겨운', '청록색', '으로', '창백', '하', '게', '바뀔', '마지막', '가로등', '난', '유영', '한다', '.', '차분', '하', '게', '과거', '에', '살', '면서', '현재', '의', '공기', '를', '마신다', '.', '가로등', '이', '깜빡인다', '.', '나', '도', ' 깜빡', '여', '준다', '.']
>>> tagger.pos("다람쥐 헌 쳇바퀴에 타고 파")
[('다람쥐', 'NNG'), ('헌', 'XSV+ETM'), ('쳇바퀴', 'NNG'), ('에', 'JKB'), ('타', 'VV'), ('고', 'EC'), ('파', 'VX+EC')]
```

# Open-source

pyeunjeon에서는 다음과 같은 오픈소스를 이용하였습니다.  
pyeunjeon used following open source projects.

* [은전한닢 프로젝트](http://eunjeon.blogspot.kr/)  
* [KoNLPy](http://konlpy.org) by Lucy Park  
* [mecab](https://github.com/taku910/mecab) by taku910  
* [mecab-python-windows](https://github.com/ikegami-yukino/mecab/releases) by ikegami-yukino  
