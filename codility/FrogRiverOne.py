'''
N개 정수로 이루어진 배열 A가 주어졌을 때, 1....X까지 모든 값이 나오는 최소 인덱스를 반환하는 solution 함수를 작성하라.

예제는 다음과 같다.

A[0] = 1
A[1] = 3
A[2] = 1
A[3] = 4
A[4] = 2
A[5] = 3
A[6] = 5
A[7] = 4

A가 다음과 같이 주어졌을 때, X값으로 5를 주면 A의 인덱스 6을 반환한다.
만약 A에서 X까지 모든 값이 없을 경우 -1을 반환한다.

효율적인 알고리즘을 제시해주길 바란다.
다음과 같은 조건에서도 작동해야 한다.

N의 범위가 [1..100,000]안에 있을 경우.
배열의 요소가 [1 ~ X] 범위 내에 있을 경우.
'''


def solution(X,A):
    '''
    O(n^2)
    '''
    idx = 0
    try:
        for i in list(range(X, 0, -1)):
            i_idx = A.index(i)
            if i_idx > idx:
                idx = i_idx
        return idx
    except ValueError as e:
        return -1

def sol(X, A):
    '''
    O(n)
    '''
    idxs = dict()
    for idx, ele in enumerate(A):
        if ele <= X:
            idxs[ele] = idx

        if len(idxs) == X:
            return idx
    return -1
X, A = (1, [1, 3, 1, 3, 6, 1, 3])
solution(X, A)
sol(X, A)

'''
영어 독해능력이 아쉬움 : 문제 이해력
n^2으로 사고하는 습성이 있는듯함
'''