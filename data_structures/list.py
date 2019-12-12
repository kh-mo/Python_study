'''
동일한 타입의 항목들
트리의 종류
- 단순연결리스트(singly linked list)
- 이중연결리스트(doubly linked list)
- 원형연결리스트(circular linked list)
'''

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError("Underflow")
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item: return k
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, '->', end=' ')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass

class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        new = self.Node(item, t, p)
        t.next = new
        p.prev = new
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        new = self.Node(item, p, t)
        p.next = new
        t.prev = new
        self.size += 1

    def delete(self, x):
        p = x.prev
        t = x.next
        p.next = t
        t.prev = p
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next

class CList:
    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_item(self): return self.size
    def is_empty(self): return self.size == 0

    def insert(self, item):
        new = self._Node(item, None)
        if self.is_empty():
            new.next = new
            self.last = new
        else:
            new.next = self.last.next
            self.last.next = new
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError("UnderFlow")
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError("UnderFlow")
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)


if __name__ == "__main__":
    s = SList()
    s.insert_front("orange")
    s.insert_front("apple")
    s.insert_after("cherry", s.head.next) # insert_after(a,b) : a를 b 다음에 오도록 한다
    s.insert_front("pear")
    s.print_list()
    print("cherry는 %d번째"%s.search("cherry")) # head가 첫번째 항목이고(이 경우 pear), apple=1, orange=2, cherry=3
    print("kiwi는", s.search("kiwi"))
    print("배 다음 노드 삭제 후:\t\t", end="")
    s.delete_after(s.head)
    s.print_list()
    print("첫 노드 삭제 후:\t\t", end="")
    s.delete_front()
    s.print_list()

    s = DList()
    s.insert_after(s.head, 'apple')
    s.insert_before(s.tail, 'orange')
    s.insert_before(s.tail, 'cherry')
    s.insert_after(s.head.next, 'pear')
    s.print_list()
    print('마지막 노드 삭제 후:\t', end='')
    s.delete(s.tail.prev)
    s.print_list()
    print('맨 끝에 포도 삽입 후:\t', end='')
    s.insert_before(s.tail, 'grape')
    s.print_list()

    s = CList()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()
    print('s의 길이 =', s.no_item())
    print('s의 첫 항목 :', s.first())
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.print_list()
    print('s의 길이 =', s.no_item())