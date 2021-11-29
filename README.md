# algorithm

### reference site
[codility](https://app.codility.com/programmers/)

### Getting Started

1. 가상환경 생성하기
- window
```bash
conda create -n algorithm python=3.8.8
conda activate algorithm
git clone https://github.com/kh-mo/algorithm.git
cd algorithm
```

- mac
```bash
pyenv install 3.8.8
pyenv virtualenv 3.8.8 algorithm
git clone https://github.com/kh-mo/algorithm.git
cd algorithm
pyenv activate algorithm
```

2. 패키지 설치하기 & pre-commit 자동화하기
```bash
# 패키지 설치
pip install -r requirements.txt
# pre-commit 자동화
pre-commit install
```