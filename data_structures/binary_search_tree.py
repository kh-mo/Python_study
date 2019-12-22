'''
이진탐색트리는 이진탐색을 위해 단순연결리스트를 변형시킨 자료구조이다.
이진탐색트리는 중위순회를 하면 정렬된 리스트를 얻는다.
이진탐색트리 조건 : 각 노드는 왼쪽 서브디렉토리보다 키값이 크고 오른쪽 서브디렉토리보다 키값이 작다
'''

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root == None:
            print("트리가 비어 있음")
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n


if __name__ == "__main__":
    t = Binary_search_tree()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
