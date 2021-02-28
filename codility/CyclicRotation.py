'''
n개 정수로 이루어진 배열 A가 있다.
Rotation이란 배열의 각 요소를 오른쪽으로 1 index 만큼 이동하는 것을 의미한다.
이 때 배열의 마지막 요소는 배열의 첫번째 요소로 이동한다.
예를들면 [3,8,9,7,6] 배열은 오른쪽으로 한 번 rotation했을 시 [6,3,8,9,7]이 된다.

배열 A와 ratation 횟수 K가 주어졌을 때 결과 배열을 반환하는 함수를 작성하라.
예제는 다음과 같다.

A = [3, 8, 9, 7, 6], K = 3, return [9, 7, 6, 3, 8]
A = [0, 0, 0], K = 1, return [0, 0, 0]
A = [1, 2, 3, 4], K = 4, return [1, 2, 3, 4]
'''

# solution 1
def solution(A, K):
    # 배열의 길이를 센다
    arr_len = len(A)

    # 해당 배열이 K와 같거나 배열의 크기가 0 또는 1이면 바로 A를 반환한다.
    if arr_len == K or arr_len == 0 or arr_len == 1:
        return A
    elif arr_len > K:
        # rotation을 수행하지 않는 경우엔 A를 그대로 반환한다.
        if K == 0:
            return A
        # 배열이 둘로 쪼개진다는 가정하에서 아래 코드가 동작한다.
        return A[-K:] + A[:(arr_len-K)]
    else:
        K %= arr_len
        return A[-K:] + A[:(arr_len-K)]

# solution 2
def solution(A, K):
    # 배열의 길이를 센다
    arr_length = len(A)
    if arr_length == 0 or K == 0:
        return A

    # K가 배열 길이보다 크면 나눠서 의미없는 회전수를 줄인다
    if K > arr_length:
        K = K % arr_length

    # 배열의 길이와 동일하면 A를 그대로 반환하고 잘라야 할 경우 앞 배열, 뒤 배열을 쪼개 합친다
    if arr_length == K:
        return A
    else:
        front_arr = A[:-K]
        back_arr = A[-K:]
        new_arr = back_arr + front_arr
        return new_arr

'''
오답노트
1. 배열이 null 배열인 경우
2. K가 0인 경우
3. lotation을 하는 의미가 없는 경우(k가 배열의 길이과 같은 경우, 배열의 길이가 1인 경우) 
''