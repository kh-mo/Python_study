'''
완전이진트리의 일종.
부모의 우선순위가 자식의 우선순위 보다 높은 자료구조.
힙속성(heap property) : 부모의 우선순위가 자식의 우선순위보다 높은 것
최소힙(minimum heap) : 키값이 작을수록 높은 우선순위
최대힙(maximum heap) : 키값이 높을수록 높은 우선순위
삭제 연산 : 루트를 삭제 후 마지막 항목을 루트로 옮긴 후 downheap
삽입 연산 : 값을 리스트 마지막 항목에 넣고 upheap
'''

class binary_heap:
    def __init__(self, li):
        self.li = li
        self.n = len(self.li) - 1

    def create_heap(self):
        for i in range(self.n//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):
        self.n += 1
        self.li.append(key_value)
        self.upheap(self.n)

    def delete_min(self):
        if self.n == 0:
            print("힙이 비어 있음")
            return None
        minimum = self.li[1]
        self.li[1], self.li[-1] = self.li[-1], self.li[1]
        del self.li[-1]
        self.n -= 1
        self.downheap(1)
        return minimum

    def downheap(self, i):
        while 2*i <= self.n:
            k = 2*i
            if k < self.n and self.li[k][0] > self.li[k+1][0]:
                k += 1
            if self.li[i][0] < self.li[k][0]:
                break
            self.li[i], self.li[k] = self.li[k], self.li[i]
            i = k

    def upheap(self, j):
        while j > 1 and self.li[j//2][0] > self.li[j][0]:
            self.li[j], self.li[j//2] = self.li[j//2], self.li[j]
            j = j//2

    def print_heap(self):
        for i in range(1, self.n+1):
            print('[%2d' % self.li[i][0], self.li[i][1], ']', end='')
        print('\n힙 크기 = ', self.n)


if __name__ == "__main__":
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    b = binary_heap(a)
    print("힙 만들기 전:")
    b.print_heap()
    b.create_heap()
    print("최소힙:")
    b.print_heap()
    print("최솟값 삭제 후")
    print(b.delete_min())
    b.print_heap()
    b.insert([5,'apple'])
    print('5 삽입 후')
    b.print_heap()


