# algorithm

### reference site
- 해외
    - [codility](https://app.codility.com/programmers/)
    - [codeforces](https://codeforces.com/)
- 국내
    - [백준](https://www.acmicpc.net/)
    - [코드업](https://codeup.kr/)
    - [프로그래머스](https://programmers.co.kr/)
    - [SW Expert Academy](https://swexpertacademy.com/main/main.do)
- 온라인 IDE
    - [리플릿](https://replit.com/)
    - [파이썬 튜터](https://pythontutor.com/)
    - [온라인 GBD](https://www.onlinegdb.com/)
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