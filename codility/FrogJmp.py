'''
X 위치에 있는 물체가 Y로 가기위해서 이동해야 하는 최대 count를 세야한다.
한 번 이동할 때 D만큼 이동하게 된다.

예를들어 X = 10, Y = 85, D = 30일 때,
10 + 30 = 40
10 + 30 + 30 = 70
10 + 30 + 30 + 30 = 100
이라면
Y보다 크거나 같은 세번째, 즉 return 3이 되어야 한다.

X,Y,D가 주어졌을 때 count를 반환하는 함수 제작
'''

import math

def solution(X, Y, D):
    return math.ceil((Y-X) / D)
