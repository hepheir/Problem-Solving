import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def make(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.make(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.make(data)

    def visit(self):
        print(self.data)

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        self.visit()


def solve():
    root = None
    for x in map(int, sys.stdin.readlines()):
        if root is None:
            root = Node(x)
        else:
            root.make(x)

    if root is not None:
        root.postorder()


solve()
