import sys

class Node:
    def __init__(self, value:int):
        self.value:int = value
        self.parent:Node = None
        self.length:int = 1
    
    def sequence(self):
        node = self
        while node is not None:
            yield node.value
            node = node.parent

N = int(sys.stdin.readline())
A = [Node(Ai) for Ai in map(int, sys.stdin.readline().split())]

for n in range(N):
    for m in range(n):
        if not (A[m].value < A[n].value):
            continue
        if A[m].length < A[n].length:
            continue
        A[n].length = A[m].length + 1
        A[n].parent = A[m]

leaf = max(A, key=lambda n: n.length)
print(leaf.length)
print(*reversed(list(leaf.sequence())))
