'''
N개 정수로 이루어진 배열 A가 주어졌을 때, 배열 A에서 나오지 않은 가장 작은 양수 정수를 반환하도록 solution 함수를 작성하라.

예제는 다음과 같다.

A = [1, 3, 6, 4, 1, 2]가 주어지면, 5를 반환한다.
A = [1, 2, 3]가 주어지면, 4를 반환한다.
A = [−1, −3]가 주어지면, 1을 반환한다.

효율적인 알고리즘을 제시해주길 바란다.
다음과 같은 조건에서도 작동해야 한다.

N의 범위가 [1..100,000]안에 있을 경우.
배열의 요소가 [−1,000,000..1,000,000] 범위 내에 있을 경우.
'''

def solution(A):
    # 음수 제거
    a = [ele for ele in A if ele>0]
    if len(a) == 0:
        return 1
    else:
        # 중복된 숫자 제거
        a = list(set(a))
        # a가 빈 숫자 없는 배열이면 최대값+1 반환
        if len(a) == max(a):
            return max(a)+1
        else:
            # 숫자가 배열에 있는지 재귀적으로 서치(exhaustive search)
            return recurArray(1, a)

def recurArray(i, a):
    if i in a:
        i += 1
        return recurArray(i, a)
    return i

'''
time complexity : O(N**2)
수정 요소
1. 재귀 배열이 파이썬은 기본 1000으로 설정되어 있다.
    -> 참고 코드 
    import sys
    sys.setrecursionlimit(10**9)
    배열의 제한 횟수를 늘려주어야 한다.
2. 시간이 너무 오래걸려서 계산효율성이 없다.
    -> 해결해야 할 부분이다.
'''