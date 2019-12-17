'''
N개의 정수로 구성된 비어있지 않은 배열 A가 있다.
어떠한 정수 P는 tape를 두 조각으로 나눈다.
[0~p-1], [p~N-1]
part1 - part2의 절대값 차이가 가장 작은 값을 반환하는 함수를 구현해라.
'''
O(N*N)
def solution(A):
    minimum_value = 1000000000000000
    fir_part = A[:1]
    sec_part = A[1:]
    fir_sum = sum(fir_part)
    sec_sum = sum(sec_part)
    diff = fir_sum - sec_sum
    while True:
        abs_diff = abs(diff)
        if abs_diff < minimum_value:
            minimum_value = abs_diff
        if len(sec_part) == 1:
            break
        diff += 2 * sec_part.pop(0)
    return minimum_value

def solution(A):
    minimum_value = 1000000000000000
    fir_sum = 0
    sec_sum = sum(A)
    for i in range(1, len(A)):
        fir_sum += A[i-1]
        sec_sum -= A[i-1]
        abs_diff = abs(fir_sum - sec_sum)
        if abs_diff < minimum_value:
            minimum_value = abs_diff
    return minimum_value

O(N)
def solution(A):
    sum_fromFist = 0
    sum_toLast = sum(A)
    minDiff = 10000000000000000000
    for P in range(1,len(A)):
        sum_fromFist += A[P-1]
        sum_toLast -= A[P-1]
        diff = abs(sum_fromFist-sum_toLast)
        if diff < minDiff:
            minDiff = diff
    return minDiff
'''
오류 리스트...
더 빠른 알고리즘이 필요하다....
1.1.672 sTIMEOUT ERROR, running time: 1.672 sec., time limit: 0.720 sec.
2.1.716 sTIMEOUT ERROR, running time: 1.716 sec., time limit: 0.752 sec.
1.0.468 sTIMEOUT ERROR, running time: 0.468 sec., time limit: 0.448 sec.
1.1.660 sTIMEOUT ERROR, running time: 1.660 sec., time limit: 0.736 sec.
2.1.652 sTIMEOUT ERROR, running time: 1.652 sec., time limit: 0.784 sec.
3.1.096 sTIMEOUT ERROR, running time: 1.096 sec., time limit: 0.608 sec.
'''
A = [3,1,2,4,3]
A = [i for i in range(100000)]
solution(A)