'''
양수 N을 입력으로 받아 이진 표현으로 만든다.
양쪽 끝이 1로 둘러쌓인 0의 갯수들 중 최대길이를 가진 것을 반환한다.

예제는 다음과 같다.

9 : 1001 -> return 2
529 : 10000100001 -> return 4
20 : 10100 -> return 1
15 : 1111 -> return 0
32 : 100000 -> return 0

N은 [1, 2,147,483,647] 범위에 있다
'''

# solution 1
def solution(N):
    # 양수를 바이너리 값으로 변경
    binary_string = "{0:b}".format(N)
    # 1이 있는 위치를 확인
    one_index_list = [i for i in range(len(binary_string)) if binary_string.startswith("1", i)]

    # 1이 하나만 등장한다면 binary gap이 없는 경우임
    if len(one_index_list) == 1:
        return 0
    else:
        length = 0
        # 1이 있는 리스트에서 n과 n+1번째 요소값의 차이가 곧 return 해야 할 값이다
        for one_idx in range(len(one_index_list)-1):
            # 9의 경우 1001로 0,3 인덱스를 가지게 되는데 이 경우를 보정하기 위해 1을 더 빼준다
            tmp_length = one_index_list[one_idx+1] - one_index_list[one_idx] - 1
            if tmp_length > length:
                length = tmp_length
        return length

# solution 2
def solution(N):
    # 양수를 바이너리 값으로 변경
    binary_rep = "{0:b}".format(N)
    # 1이 있는 위치를 확인
    one_list = [idx for idx, bin in enumerate(binary_rep) if bin == '1']

    # 1이 0개 또는 1개면 0을 리턴
    if len(one_list) <= 1:
        return 0

    # 1로 둘러싸인 0의 개수를 세서 리턴
    # '인덱스 차이 - 1' 하면 0의 개수가 나온다
    # ex) 1010 -> (2-0) - 1 = 1
    max = 0
    if len(one_list) > 1:
        for f, e in zip(one_list[:-1], one_list[1:]):
            bin_length = e-f-1
            if max < bin_length:
                max = bin_length
        return max

