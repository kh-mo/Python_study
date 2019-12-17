'''
N개 다른 정수로 구성된 배열 A가 있다.
배열은 [1.. (N+1)]요소를 가지고 있는데 이 말은 요소 한개가 빠져있다는 뜻이다.
빠진 요소를 찾는 함수를 작성하라.

예시)
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
return 4

****** 중요 ******
demo_ver2와 동일한 문제, 같은 솔루션으로 100% 획등
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
            # 배열 정렬
            a = sorted(a)
            start_point = 0
            # 리스트 절반씩 쳐내기
            while True:
                if start_point + 1 != a[0]:
                    return start_point + 1
                else:
                    start_point, a = split_arr(start_point, a)

def split_arr(start_point, a):
    split_idx = int(len(a)/2)
    forward_arr = a[:split_idx]
    backward_arr = a[split_idx:]
    if (start_point + len(forward_arr)) == max(forward_arr):
        return max(forward_arr), backward_arr
    else:
        return start_point, forward_arr