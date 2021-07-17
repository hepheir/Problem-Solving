import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


    def visit(self):
        sys.stdout.write(self.name)


    def preorder(self):
        self.visit()
        if (self.left is not None): self.left.preorder()
        if (self.right is not None): self.right.preorder()


    def inorder(self):
        if (self.left is not None): self.left.inorder()
        self.visit()
        if (self.right is not None): self.right.inorder()


    def postorder(self):
        if (self.left is not None): self.left.postorder()
        if (self.right is not None): self.right.postorder()
        self.visit()


def make_tree(vertices):
    graph = dict()

    graph['.'] = None
    for i in range(vertices):
        name = chr(ord('A')+i)
        graph[name] = Node(name)

    for i in range(vertices):
        node, left, right = sys.stdin.readline().split()
        graph[node].left = graph[left]
        graph[node].right = graph[right]
    return graph


def solve():
    N = int(sys.stdin.readline())
    root:Node = make_tree(N)['A']

    root.preorder()
    print()

    root.inorder()
    print()

    root.postorder()
    print()

solve()