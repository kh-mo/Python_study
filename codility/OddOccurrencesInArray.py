'''
N개 정수로 이루어진 배열 A가 주어졌다.
각 요소는 홀수이고, 대부분 2개 이상 pair를 가지지만 딱 하나 pair가 아닌 숫자가 있다.
그 숫자를 반환하는 효율적인 알고리즘을 제시해주길 바란다.

예제는 다음과 같다.

A[0] = 9  A[1] = 3  A[2] = 9 A[3] = 3  A[4] = 9  A[5] = 7 A[6] = 9

위 A 배열에서 유일하게 pair가 없는 7을 반환해야 한다.
본 문제는 다음과 같은 조건에서도 작동해야 한다.

배열 크기는 홀수 정수이며 [1..1,000,000]안에 있다.
배열의 요소는 [1..1,000,000,000] 범위 내에 있다.
A 배열 중 한 요소를 제외한 다른 숫자는 짝수번 발생한다 => 한 숫자는 홀수번 반복한다는 의미다(line 29가 문제였다)
'''

from collections import Counter

def solution(A):
    if len(A) == 1:
        return A[0]

    dic = Counter()
    for i in A:
        dic[i] += 1

    for key, value in dic.items():
        if value%2 == 1:
            return key
