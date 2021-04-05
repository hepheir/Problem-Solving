import sys

sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node == None:
            node = Node(data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        else:
            node.left = self._insert(node.left, data)
        return node

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            if node.left != None:
                self._postorder(node.left)
            if node.right != None:
                self._postorder(node.right)
            print(node.data)


def solve():
    bst = BinarySearchTree()
    for data in map(int, sys.stdin.readlines()):
        bst.insert(data)
    bst.postorder()


solve()
