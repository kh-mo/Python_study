# algorithm
1. 시간 복잡도, 공간 복잡도의 Big-O 표기법

|빅오 표기법|명칭|
|---|---|
|O($1$)|상수 시간(Constant time)|
|O($logN$)|로그 시간(Log time)|
|O($N$)|선형 시간|
|O($NlogN$)|로그 선형 시간|
|O($N^2$)|이차 시간|
|O($N^3$)|삼차 시간|
|O($2^n$)|지수 시간|

간단한 예시
- 시간 제한이 1초인 문제의 경우
    - N의 범위가 500인 경우 : 시간 복잡도가 $O(N^3)$인 알고리즘을 설계하면 문제를 풀 수 있다.
    - N의 범위가 2,000인 경우 : 시간 복잡도가 $O(N^2)$인 알고리즘을 설계하면 문제를 풀 수 있다.
    - N의 범위가 100,000인 경우 : 시간 복잡도가 $O(NlogN)$인 알고리즘을 설계하면 문제를 풀 수 있다.
    - N의 범위가 10,000,000인 경우 : 시간 복잡도가 $O(N)$인 알고리즘을 설계하면 문제를 풀 수 있다.

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
- 교재
    - 이것이 취업을 위한 코딩 테스트다 ([깃헙](https://github.com/ndb796/python-for-coding-test) | [정오표](https://www.hanbit.co.kr/store/books/look.php?p_code=B8945183661))

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