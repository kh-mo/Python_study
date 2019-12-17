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

******* 중요 *******
demo.py에서 작성한 알고리즘은 계산 효율성 부족으로 66% 정도의 성능 이상을 얻지 못했다.
이를 해결하는 다른 알고리즘을 작성하고자 해당 파일을 작성한다.

리스트를 절반씩 쳐내는 알고리즘
절반으로 나눠 앞부분에 빈공간이 있으면 앞부분을 선택, 없으면 뒷부분을 선택, 그러면서 start point를 유지
계속해서 리스트를 쪼개다보면 start point와 배열사이에 빈 공간이 발생하게 된다.
해당 빈 공간이 없는 숫자다.
=> start_point + 1 != a[0]
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
