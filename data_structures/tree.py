'''
key:{왼쪽 자식, 오른쪽 형제}
트리의 종류
- 트리(tree)
- 이진트리(binary tree)
- 포화이진트리(full binary tree)
- 완전이진트리(complete binary tree)
- 편향, 경사이진트리(skewed binary tree)
- 스레드 이진트리(threaded binary tree)
순회(traversal)
노드 방문의 의미
- 전위순회(preorder) : 도착지점 방문 후 왼쪽 노드로 순회, 이후 오른쪽으로 순회
- 중위순회(inorder) : 도착지점 방문을 미루고 왼쪽으로 먼저, 오른쪽 노드는 도착지점 본 후 이동
- 후위순회(postorder) : 도착지점 방문을 미루고 왼쪽을 먼저 보고 오른쪽을 본 후 도착지점 탐색
- 레벨순회(levelorder) : 레벨별로 왼쪽에서 오른쪽으로 탐색
'''

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        # 높이 구하기
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

    def preorder(self, n):
        # 전위순회
        if n != None:
            print(str(n.item),' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ',end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ',end='')

    def levelorder(self, root):
        # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

if __name__ == "__main__":
    t = BinaryTree()
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)
    n5 = Node(500)
    n6 = Node(600)
    n7 = Node(700)
    n8 = Node(800)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8

    t.root = n1
    print("트리 높이 =", t.height(t.root))
    print("전위순회:\t", end='')
    t.preorder(t.root)
    print("중위순회:\t", end='')
    t.inorder(t.root)
    print("후위순회:\t", end='')
    t.postorder(t.root)
    print("레벨순회:\t", end='')
    t.levelorder(t.root)