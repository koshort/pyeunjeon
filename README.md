# pyeunjeon (python + eunjeon)

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

Install mecab first.  
mecab을 먼저 설치해주세요.  
[mecab installer by ikegami-yukino](https://github.com/koshort/peunjeon/releases/download/0.996/mecab-0.996-64.exe)

```bash
pip install eunjeon
```

# Usage 사용법
```python
from eunjeon import Mecab  # KoNLPy style mecab wrapper

tagger = Mecab() 
tagger.nouns("고양이가 냐 하고 울면 나는 녜 하고 울어야지")
> ['고양이', '나', '녜']
```

# Open-source

pyeunjeon에서는 다음과 같은 오픈소스를 이용하였습니다.  
pyeunjeon used following open source projects.

* [은전한닢 프로젝트](http://eunjeon.blogspot.kr/)  
* [KoNLPy](http://konlpy.org) by Lucy Park  
* [mecab](https://github.com/taku910/mecab) by taku910  
* [mecab-python-windows](https://github.com/ikegami-yukino/mecab/releases) by ikegami-yukino  
